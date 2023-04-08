<template>
  <div class="box">
    <div
        v-for="i in 5"
        :key="i"
    >
      <h3>ТОС-{{ i }}</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
        est
        laborum.
      </p>
      <ul>
        <li>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit
        </li>
        <li>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
          dolore
          magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex
        </li>
        <li>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit
        </li>
      </ul>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore
        magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
        pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id
        est
        laborum.
      </p>
      <hr>
    </div>
  </div>
</template>

<script>
export default {
  name: "TASText",
}
</script>

<style lang="scss" scoped>

.box {
  //display: block;
  overflow-x: visible;
  white-space: break-spaces;
  position: relative;
  min-width: 100%;
  height: calc(100vh - 300px);
  overflow-y: auto;
}


</style>