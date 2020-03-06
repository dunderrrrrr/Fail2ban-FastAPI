<template>
  <div id="app">
    <div class="wrapper">
      <nav id="sidebar">
        <div class="sidebar-header">
            <h3>Fail2ban FastAPI</h3>
        </div>
        <ul class="list-unstyled components">
          <p>For easy management.</p>
          <span v-if="curr_route == 'Home'">
            <li class="active"><router-link :to="{ name: 'Home' }">Home</router-link></li>
          </span>
          <span v-else>
            <li><router-link :to="{ name: 'Home' }">Home</router-link></li>
          </span>
          <span v-if="curr_route == 'Jails'">
            <li class="active"><router-link :to="{ name: 'Jails' }">Jails</router-link></li>
          </span>
          <span v-else>
            <li><router-link :to="{ name: 'Jails' }">Jails</router-link></li>
          </span>
        </ul>
        <ul class="list-unstyled CTAs">
          <li>
            <a href="https://bootstrapious.com/tutorial/files/sidebar.zip" class="download"><font-awesome-icon icon="download"/> Download source</a>
          </li>
        </ul>
      </nav>
      <div id="content">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>
<script>
require('../static/main.css')

export default {
  name: 'app',
  data () {
    return {
      curr_route:''
    }
  },
  created() {
    this.curr_route = this.$route.name
  },
  watch: {
    '$route': 'checkRoute'
  },
  methods: {
    checkRoute () {
      this.curr_route = this.$route.name
    },
  }
}
</script>