<template>
    <div class="post-item">
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
        <div v-if="typeof post.comments === 'string'">
            <Comment :comment="{author: '', content: post.comments}" />
        </div>
        <Comment v-else v-for="comment in post.comments" :key="comment.id" :comment="comment" />
    </div>
</template>

<script>
import Comment from './PostComment.vue'

export default {
    props: {
        post: Object
    },
    components: {
        Comment,
    },
}
</script>



<!--Всё что ниже - уже не актуально, оставил в память об уроке, просто собрал новую сборку и отправил с dist в бэк-->--> 
<style scoped>
.post-item {
	border: 1px solid #ccc;
	padding: 15px;
	margin: 20px;
	border-radius: 8px;
	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.post-item h2 {
	font-size: 24px;
	color: blue;
}

.post-item p {
	color: red;
	font-size: 16px;
}
</style>