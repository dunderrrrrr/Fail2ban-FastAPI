<template>
  <div class="row">
    <div class="col-md-12">
      <h1>Jail [{{jail_name}}]</h1>
      <div v-if="jail_data['error']">
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
          Cannot connect to API - is it running?
          <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
      </div>
      <div class="card mb-3"  v-for="data in jail_data">
        <div class="card-body">
          <p class="card-text">{{data.log_file}}</p>
        </div>
      </div>
    </div>
    <div class="col-sm-3" v-for="data in jail_data">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Current bans</h5>
          <h1 class="text-center">{{data.bans_current}}</h1>
        </div>
      </div>
    </div>
    <div class="col-sm-3" v-for="data in jail_data">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Total bans</h5>
          <h1 class="text-center">{{data.bans_total}}</h1>
        </div>
      </div>
    </div>    
    <div class="col-sm-3" v-for="data in jail_data">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Current fails</h5>
          <h1 class="text-center">{{data.fails_current}}</h1>
        </div>
      </div>
    </div>
    <div class="col-sm-3" v-for="data in jail_data">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Total fails</h5>
          <h1 class="text-center">{{data.fails_total}}</h1>
        </div>
      </div>
    </div>
    <div class="col-sm-6 mt-3">
      <h4 class="float-left">Banned IPs</h4> 
      <div class="float-right p-1"><a href="#" @click="refreshData">Refresh <font-awesome-icon icon="sync-alt"/></a></div>
      <input type="text" v-model="search" class="form-control" placeholder="Search IP">
      <div class="mt-2">
        <div v-for="(ip, index) in filterIPs" class="delObjects p-1 m-1">
            {{ip}} <a href="#" v-on:click.prevent="deleteObject(ip, index)">&times;</a>
        </div>
      </div>
    </div>
    <div class="col-sm-6 mt-3">
      <h4>Ban IP</h4>
      <notifications group="banStatus" />
      <form class="form-inline" v-on:submit="banIP" action="#">
        <input type="text" v-model="banningIP"  class="form-control mb-2 mr-sm-2" placeholder="xxx.xxx.xxx.xxx">
        <button type="submit" class="btn btn-secondary mb-2">Ban</button>
      </form>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

require('../../static/main.css')

export default {
  name: 'Jails',
  components: {
    axios
  },
  data () {
    return {
      jail_data: "",
      jail_name: this.$route.params.jailname,
      banlist: "",
      search: "",
      banningIP: "",
      banStatus: ""
    }
  },
  created () {
    this.getJails()
  },
  watch: {
    '$route': 'getJails'
  },
  methods: {
    getJails () {
      const url = `${window.location.protocol}//${window.location.hostname}/api/jail/${this.jail_name}`;
      axios.get(url)
        .then((resp) => {
          this.jail_data = resp.data
          for (let key in resp.data) {
              this.banlist = resp.data[key].bans_iplist
            }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    refreshData() {
      this.getJails()
    },
    ValidateIPaddress(ipaddress) {
      if (/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(ipaddress))
      {return (true)}
      else {return (false)}
    },
    banIP: function(event){
      let validIP = this.ValidateIPaddress(this.banningIP)
      if (this.banningIP) {
        if (validIP) {
          // POST ban
          const url = `${window.location.protocol}//${window.location.hostname}/api/ban`;
          axios.post(url, {
              'ip': this.banningIP,
              'jail': this.jail_name,
            })
            .then(function (response) {
              console.log(response);
            })
          .catch(function (error) {
            console.log(error);
          });
          // refresh jail needs to wait a lil?
          this.getJails();
          // notify
          this.$notify({
            group: 'banStatus',
            title: 'Success!',
            text: '<b>' + this.banningIP + '</b>' + ' has been banned in jail <b>' + this.jail_name + '</b>',
            type: 'success'
          });
        } else {
          this.$notify({
            group: 'banStatus',
            title: 'Error!',
            text: '<b>' + this.banningIP + '</b>' + ' is not a valid IP-address.',
            type: 'error'
          });
        }
      } else {
        this.$notify({
          group: 'banStatus',
          title: 'Error!',
          text: 'You have to input something dummy.',
          type: 'warn'
        });        
      }
    },   
    deleteObject: function(ip, index) {
      this.$delete(this.banlist, index);
      console.log(this.banlist)
      // POST unban
      const url = `${window.location.protocol}//${window.location.hostname}/api/unban`;
      axios.post(url, {
          'ip': ip,
          'jail': this.jail_name,
        })
        .then(function (response) {
          console.log(response);
        })
      .catch(function (error) {
        console.log(error);
      });
      // refresh jail
      this.getJails()
      // notify      
      this.$notify({
        group: 'banStatus',
        title: 'Success!',
        text: '<b>' + ip + '</b>' + ' has been unbanned in jail <b>' + this.jail_name + '</b>',
        type: 'success'
      });      
    },
  },
  computed: {
    filterIPs: function() {
      let filtered = this.banlist;
      if (this.search) {
        filtered = this.banlist.filter(
          m => m.toLowerCase().indexOf(this.search.toLowerCase()) > -1,
        );
      }
      return filtered;
    },     
  }
}
</script>
