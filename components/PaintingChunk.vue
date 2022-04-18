<template>
  <div
    :style="{
      width: paintingPiece.dimensions.width + 'px',
      height: paintingPiece.dimensions.height + 'px',
    }"
    class="painting-chunk"
    :class="[
      'bg-' + color,
      changeable ? 'hover:bg-' + color + '-dark changable' : '',
    ]"
    @click="changeable ? flip() : null"
  >
    <img v-if="revealed" :src="paintingPiece.src" />
  </div>
</template>

<script>
export default {
  name: 'PaintingItem',
  props: {
    paintingPiece: {
      type: Object,
      required: true,
    },
    color: {
      type: String,
      required: true,
    },
    changeable: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      revealed: false,
    }
  },
  methods: {
    flip() {
      this.$emit('revealed', this.paintingPiece)
      this.revealed = true
    },
  },
}
</script>

<style scoped>
.changable:hover {
  box-shadow: 0 0 10px rgb(70 70 70) inset;
}
</style>