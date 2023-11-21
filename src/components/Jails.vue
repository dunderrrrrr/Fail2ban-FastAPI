<template>
  <div class="row">
    <div class="col-md-12">
      <div v-if="apistatus == false">
        <div class="alert alert-danger alert-dismissible fade show" role="alert">
          Cannot connect to API - is it running?
          <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
      </div>     
    </div>
    <div class="col-sm-12 mt-3" v-for="jail in jails">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title float-left">{{jail.jail_name}}</h5>
          <div class="float-right pl-3">
            <p class="card-text logPath">{{jail.log_file}}</p>
          </div>
          <div class="row clearBoth">
            <div class="col-sm-3">
              <p class="card-text border-bottom">Current bans: <b>{{jail.bans_current}}</b></p>
            </div>
            <div class="col-sm-3">
              <p class="card-text border-bottom">Total bans: <b>{{jail.bans_total}}</b></p>
            </div>
            <div class="col-sm-3">
              <p class="card-text border-bottom">Current fails: <b>{{jail.fails_current}}</b></p>
            </div>
            <div class="col-sm-3">
              <p class="card-text border-bottom">Total fails: <b>{{jail.fails_total}}</b></p>
            </div>
            <div class="col-sm-12 mt-2">
              <a v-bind:href="'/jail/'+jail.jail_name">
                <button type="button" class="btn btn-dark btn-sm">Manage bans</button>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'Jails',
  components: {
    axios
  },
  data () {
    return {
      jails: "",
      apistatus: 'true',
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
      const url = `${window.location.protocol}//${window.location.hostname}/api/jails`;
      axios.get(url)
        .then((resp) => {
          this.apistatus = true
          this.jails = resp.data.jail
        })
        .catch((err) => {
          this.apistatus = false
          console.log(err)
        })
    },
  }
}
</script>
