<template>
  <div @click="show = !show" class="rounded-xl shadow-lg mt-10 w-1/3 m-3 h-12">
    <div class="flex justify-between p-3">
      <h1>{{ title }}</h1>
      <box-icon
        :class="show ? 'rotate-180' : ''"
        type="solid"
        name="down-arrow"
      ></box-icon>
    </div>
    <div v-if="show" class="p-5 rounded-xl shadow-xl"><slot></slot></div>
  </div>
</template>
<script>
export default {
  props: { title: String, body: String },
  data() {
    return {
      show: false,
    };
  },
};
</script>
