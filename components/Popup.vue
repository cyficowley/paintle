<template>
  <div
    v-if="visible"
    class="
      fixed
      h-screen
      w-screen
      top-0
      left-0
      flex
      justify-center
      items-center
    "
    @click.self="$emit('close')"
  >
    <div class="bg-white rounded-lg p-8 max-w-lg shadow relative">
      <div
        class="absolute right-0 top-0 p-2 m-2 cursor-pointer"
        @click="$emit('close')"
      >
        <svg height="25" width="25">
          <g transform="translate(3.9661017,3.5677966)">
            <path
              stroke="rgb(107, 114, 128)"
              stroke-width="3"
              d="M -2.5783352e-4,-0.00146808 17.435473,18.212367"
            />
            <path
              stroke="rgb(107, 114, 128)"
              stroke-width="3"
              d="M -2.5783352e-4,18.212367 17.435473,-0.00146808"
            />
          </g>
        </svg>
      </div>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    visible: {
      type: Boolean,
      default: false,
    },
  },
}
</script>