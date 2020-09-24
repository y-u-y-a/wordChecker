import Vue from 'vue';
import VueAxios from 'vue-axios';
import axios from 'axios';

import App from '@/App';
import Router from '@/route/index';
import Store from '@/store/index';
import 'bootstrap/dist/css/bootstrap.css';

Vue.config.productionTip = false
Vue.use(VueAxios, axios)
axios.defaults.baseURL = 'http://localhost:8000'
// // add CSRF Token
// axios.defaults.xsrfCookieName = 'csrftoken';
// axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';


new Vue({
  render: h => h(App),
  router: Router,
  store: Store,
}).$mount('#app');
