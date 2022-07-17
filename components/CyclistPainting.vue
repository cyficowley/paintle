<template>
  <div
    ref="painting-container"
    class="flex items-center justify-center h-full overflow-hidden"
  >
    <div
      class="relative bg-white"
      :style="{ width: imageScaledDimensions.width + 'px' }"
      style="font-size: 0"
    >
      <CyclistPaintingChunk
        v-for="(imagePiece, index) in imagePieces"
        :key="imagePiece.id"
        class="inline-block"
        :painting-piece="imagePiece"
        :color="colors[index % colors.length]"
        :changeable="changeable"
        :reveal="reveal"
        @revealed="handleReveal"
      />
    </div>
  </div>
</template>


<script>
const debounce = require('debounce')

export default {
  name: 'CyclePaintingItem',
  props: {
    painting: {
      type: Object,
      required: true,
    },
    changeable: {
      type: Boolean,
      required: true,
    },
    reveal: {
      type: Boolean,
      required: true,
    },
  },
  data() {
    return {
      imagePieces: [],
      cols: 4,
      rows: 4,
      containerDimensions: { width: 0, height: 0 },
      imageScaledDimensions: { width: 0, height: 0 },
      colors: ['purpley', 'goldy', 'cyany', 'reddy', 'browny'],
    }
  },
  computed: {
    filteredPaintings() {
      const filteredPaintings = this.allAnswers.filter((painting) => {
        // checks if the painting name or artist contains the search term
        return painting.name.toLowerCase().includes(this.message.toLowerCase())
      })
      return filteredPaintings
    },
  },
  watch: {
    painting: {
      handler(painting) {
        this.slicePainting(painting)
      },
    },
  },
  created() {
    // eslint-disable-next-line nuxt/no-globals-in-created
    window.addEventListener('resize', debounce(this.setDimensions, 100))
  },
  mounted() {
    this.setDimensions()
  },
  methods: {
    slicePainting(painting) {
      const cutImageUp = (image) => {
        const imagePieces = []

        const numColsToCut = this.cols
        const numRowsToCut = this.rows

        const ratioWidth = image.width / this.containerDimensions.width
        const ratioHeight = image.height / this.containerDimensions.height

        const ratio = Math.max(ratioWidth, ratioHeight, 1)

        this.imageScaledDimensions = {
          width: image.width / ratio,
          height: image.height / ratio,
        }

        const widthOfOnePiece = image.width / numColsToCut
        const heightOfOnePiece = image.height / numRowsToCut

        let id = 0

        for (let y = 0; y < numRowsToCut; ++y) {
          for (let x = 0; x < numColsToCut; ++x) {
            const canvas = document.createElement('canvas')
            canvas.width = widthOfOnePiece / ratio
            canvas.height = heightOfOnePiece / ratio
            const context = canvas.getContext('2d')

            context.drawImage(
              image,
              x * widthOfOnePiece,
              y * heightOfOnePiece,
              widthOfOnePiece,
              heightOfOnePiece,
              0,
              0,
              canvas.width,
              canvas.height
            )
            imagePieces.push({
              id,
              col: x,
              row: y,
              dimensions: { width: canvas.width, height: canvas.height },
              src: canvas.toDataURL(),
            })
            id++
          }
        }
        this.imagePieces = imagePieces
      }

      const image = new Image()
      image.onload = () => cutImageUp(image)
      image.src = painting.path
      console.log('painting.path')
      console.log(painting.path)
    },

    setDimensions() {
      const paintingContainer = this.$refs['painting-container']
      this.containerDimensions.height = paintingContainer.clientHeight
      this.containerDimensions.width = paintingContainer.clientWidth
      this.slicePainting(this.painting)
    },

    handleReveal(paintingPiece) {
      this.$emit('revealed', paintingPiece.id)
    },
  },
}
</script>
