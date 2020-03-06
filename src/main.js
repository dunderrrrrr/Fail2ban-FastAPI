// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faBookDead, faSkull, faCaretRight, faArchway, faDownload, faSyncAlt } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import Notifications from 'vue-notification'

Vue.config.productionTip = false

Vue.use(Notifications)

library.add(
  faBookDead,
  faSkull,
  faCaretRight,
  faArchway,
  faDownload,
  faSyncAlt
)

Vue.component(
  'font-awesome-icon', 
  FontAwesomeIcon
)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
