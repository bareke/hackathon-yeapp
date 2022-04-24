<template>
  <div
    class="shadow-xl w-10/12 mt-5 flex flex-col justify-center gap-4 items-center w-full rounded-xl pb-4"
  >
    <div class="w-full">
      <step-progress
        :steps="steps"
        :current-step="currentStep"
        icon-class="fa fa-check"
        active-color="blue"
      ></step-progress>
    </div>
    <h1 v-if="currentStep === 0" class="text-4xl mb-4">
      Registrar nueva historia clinica
    </h1>
    <keep-alive>
      <FormUserInfo
        v-if="currentStep === 1"
        @user-data="loadUserData($event)"
      />
    </keep-alive>
    <keep-alive>
      <ConsultReason
        v-if="currentStep === 2"
        @consult-data="loadConsultData($event)"
      />
    </keep-alive>
    <keep-alive>
      <UserAnnexes v-if="currentStep === 3" />
    </keep-alive>

    <div class="flex gap-5">
      <vs-button type="filled" @click="back" v-if="currentStep > 0">
        <box-icon name="left-arrow" type="solid" color="#fff"></box-icon
        >Anterior</vs-button
      >
      <div v-if="currentStep < 4">
        <vs-button type="filled" @click="next"
          >Siguiente
          <box-icon name="right-arrow" type="solid" color="#fff"></box-icon
        ></vs-button>
      </div>
      <div v-else>
        <vs-button size="xl" success type="filled" @click="register"
          >Registrar</vs-button
        >
      </div>
    </div>
  </div>
</template>
<script>
import StepProgress from "vue-step-progress";
import "vue-step-progress/dist/main.css";
import FormUserInfo from "./FormUserInfo.vue";
import ConsultReason from "./ConsultReason.vue";
import UserAnnexes from "./UserAnnexes.vue";
export default {
  components: {
    "step-progress": StepProgress,
    FormUserInfo,
    ConsultReason,
    UserAnnexes,
  },
  data() {
    return {
      steps: [
        "Inicio",
        "Datos del paciente",
        "Datos de la consulta",
        "Anexos",
        "Enviar",
      ],
      currentStep: 0,
      notification: null,

      form: {
        data: {
          userData: {},
          consultData: {},
        },
      },
    };
  },
  methods: {
    next() {
      this.currentStep++;
    },
    back() {
      this.currentStep--;
    },
    register() {
      this.$apollo
        .mutate({
          mutation: require("@/graphql/CreateClinicHistory.gql"),
          variables: {
            data: this.form,
          },
        })
        .then(() => {
          this.currentStep = 0;
          (this.form.data = {}),
            this.launchNotification(
              "success",
              "Historia registrada",
              "...",
              '<box-icon color="rgb(20,255,20)" type="solid" name="newUser-check"></box-icon>'
            );
        })
        .catch(() => {
          this.error = true;
          this.launchNotification(
            "danger",
            "Registro fallído",
            "Revisa los datos ingresados.",
            '<box-icon name="newUser-check" color="#e81519" ></box-icon>'
          );
        });
    },

    loadUserData(ev) {
      this.form.data.userData = ev;
    },
    loadConsultData(ev) {
      this.form.data.consultData = ev;
    },
    launchNotification(color = "success", title = "", body = "", icon = "") {
      this.$vs.notification({
        position: "top-right",
        color,
        flat: true,
        icon,
        progress: "auto",
        title,
        text: body,
      });
    },
  },
};
</script>
<style>
.step-progress__step-label {
  font-size: 10px;
}
.step-progress__step:after {
  width: 50px;
  height: 50px;
}
.step-progress__step span {
  font-size: 30px;
}
</style>
