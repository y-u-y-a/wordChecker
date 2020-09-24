<template>
  <div class="bg-success">
    <TheHeader />
    <main class="container-fluid bg-white">
      <RouterView />
    </main>
    <TheFooter />
  </div>
</template>


<script>
import TheHeader from '@/components/common/TheHeader'
import TheFooter from '@/components/common/TheFooter'

export default {
  components: {
    TheHeader,
    TheFooter
  }
}
</script>


<style lang="scss">
// HACK: babelでsassファイルを読み込みたい
@import '@/assets/sass/app.scss';
</style>
