import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import { createProvider } from "./vue-apollo";
import Vuesax from "vuesax";
import "vuesax/dist/vuesax.css"; //Vuesax styles
import "boxicons";

import StepProgress from "vue-step-progress";

// import the css (OPTIONAL - you can provide your own design)
import "vue-step-progress/dist/main.css";
import "@/assets/styles/index.css";

Vue.config.productionTip = false;
Vue.use("step-progress", StepProgress);
Vue.use(Vuesax, {
  // options here
});

new Vue({
  components: {
    "step-progress": StepProgress,
  },
  router,
  store,
  apolloProvider: createProvider(),
  render: (h) => h(App),
}).$mount("#app");
