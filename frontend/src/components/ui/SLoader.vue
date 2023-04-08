<template>
  <div class="loader"></div>
</template>

<script>
export default {
  name: "SLoader"
}
</script>

<style lang="scss" scoped>

.loader,
.loader:after {
  border-radius: 50%;
  width: 4em;
  height: 4em;
}

.loader {
  margin: 60px auto;
  font-size: 10px;
  position: relative;
  text-indent: -9999em;
  border-top: 0.3em solid white;
  border-right: 0.3em solid white;
  border-bottom: 0.3em solid white;
  border-left: 0.3em solid $Base1;
  -webkit-transform: translateZ(0);
  -ms-transform: translateZ(0);
  transform: translateZ(0);
  -webkit-animation: load8 1.1s infinite linear;
  animation: load8 1.1s infinite linear;
}

@-webkit-keyframes load8 {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

@keyframes load8 {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

</style>