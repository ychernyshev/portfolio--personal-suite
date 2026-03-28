import { ref } from 'vue';

export function useNumberAnimation() {
    const animatedNumber = ref(0);

    const animate = (target, duration = 1000) => {
        const start = animatedNumber.value;
        const end = parseFloat(target);
        const startTime = performance.now();

        const update = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);

            const easeOut = (t) => t * (2 - t);

            animatedNumber.value = start + (end - start) * easeOut(progress);

            if (progress < 1) {
                requestAnimationFrame(update);
            } else {
                animatedNumber.value = end;
            }
        };

        requestAnimationFrame(update);
    };

    return {
        animatedNumber,
        animate
    };
}