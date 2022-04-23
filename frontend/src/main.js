import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import { createProvider } from "./vue-apollo";
import Vuesax from "vuesax";
import "vuesax/dist/vuesax.css"; //Vuesax styles
import "boxicons";

import "@/assets/styles/index.css";

Vue.config.productionTip = false;

Vue.use(Vuesax, {
  // options here
});

new Vue({
  router,
  store,
  apolloProvider: createProvider(),
  render: (h) => h(App),
}).$mount("#app");
