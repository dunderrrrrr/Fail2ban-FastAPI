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
    <div class="col-sm-4">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Active Jails</h5>
          <h1 class="text-center">{{summary.jail_nums}}</h1>
          <p class="card-text">Total number of active jails.</p>
          <a href="/jails" class="btn btn-primary"><font-awesome-icon icon="archway"/> Show jails</a>
        </div>
      </div>
    </div>
    <div class="col-sm-4">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Current bans</h5>
          <h1 class="text-center">{{summary.total_bans_current}}</h1>
          <p class="card-text">Currently banned IPs.</p>
          <a href="/jails" class="btn btn-primary"><font-awesome-icon icon="skull"/> Manage bans</a>
        </div>
      </div>
    </div>
    <div class="col-sm-4">
      <div class="card">
        <div class="card-body">
          <h5 class="card-title">Total bans</h5>
          <h1 class="text-center">{{summary.total_bans_total}}</h1>
          <p class="card-text">Total amount of bans.</p>
          <a href="/jails" class="btn btn-primary"><font-awesome-icon icon="book-dead"/> Show bans</a>
        </div>
      </div>  
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'Home',
  data () {
    return {
      summary: '',
      apistatus: 'true',
    }
  },
  created () {
    this.getSummary()
  },
  watch: {
    '$route': 'getSummary'
  },  
  methods: {
    getSummary () {
      const url = `${window.location.protocol}//${window.location.hostname}/api/jails`;
      axios.get(url)
        .then((resp) => {
          this.apistatus = true
          this.summary = resp.data.sum
        })
        .catch((err) => {
          console.log(err)
          this.apistatus = false
        })
    }
  }
}
</script>
