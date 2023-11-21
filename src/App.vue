<template>
  <div id="app">
    <div class="wrapper">
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
