<template lang="pug">
  v-app
    v-app-bar(app='' color='green' dark='')
      .d-flex.align-center
        v-img.shrink.mr-2(alt='Vuetify Logo' contain='' src='https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png' transition='scale-transition' width='40')
          v-img.shrink.mt-1.hidden-sm-and-down(alt='Vuetify Name' contain='' min-width='100' src='https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png' width='100')
      v-spacer
      v-btn(href='https://github.com/vuetifyjs/vuetify/releases/latest' target='_blank' text='')
        span.mr-2 Latest Release
        v-icon mdi-open-in-new
    v-main
      router-view

</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'App',

  data: () => ({
    //
  }),
});
</script>
