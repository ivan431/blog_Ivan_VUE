<template>
    <div class="post-list">
        <post-item v-for="post in posts" :key="post.id" :post="post">
        </post-item>
    </div>
</template>

<script>
import PostItem from './PostItem.vue';

export default {
    components: {
        PostItem,
    },

    props: {
        posts: Array
    }
}
</script>
