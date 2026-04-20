<script setup lang="ts">
import { computed } from 'vue';
import { useRouter } from 'vue-router';

const props = defineProps<{
  to?: string;
  href?: string;
  type?: 'button' | 'submit' | 'reset';
  title: string;
}>();

const router = useRouter();

const extraAttrs = computed(() => {
  if (tag.value === 'a' && props.href?.startsWith('http')) {
    return { target: '_blank', rel: 'noopener noreferrer' };
  }
  return {};
});

const tag = computed(() => {
  if (props.to) {
    const exists = router.getRoutes().some(r => r.path === props.to);
    return exists ? 'router-link' : 'a';
  }
  if (props.href) return 'a';
  return 'button';
});
</script>

<template>

  <component
      :is="tag"
      :to="tag === 'router-link' ? to : null"
      :href="tag === 'a' ? (href || to) : null"
      :type="tag === 'button' ? type : null"
      v-bind="extraAttrs"
      class="btn btn-transform border-0"
  >
    <slot name="left"></slot>
    <span>{{ title }}</span>
    <slot name="right"></slot>
    <slot></slot>
  </component>
</template>

<style scoped>
  .shift-icon {}
  .shift-icon:hover {
     margin-right: .4rem;
     transition: .5s;
  }

  .btn {
    font-size: clamp(1.4rem, 1.4vw, 1.4rem);
  }
</style>