<template>
	<div id="app">
		<Header />
		<main>
			<post-list :posts="posts"></post-list>
		</main>
		<Footer />
	</div>
</template>

<script>
import Header from './components/BlogHeader.vue';
import Footer from './components/BlogFooter.vue';
import PostList from './components/PostList.vue';
import axios from 'axios';

export default {
	name: 'App',
	components: {
		Header,
		Footer,
		PostList
	},
	data() {
		return {
			posts: []
		}
	},
	created() {
		this.fetchPosts();
	},
	methods: {
		async fetchPosts() {
			try {
				const response = await axios.get('/api/posts');
				this.posts = response.data;
			} catch (error) {
				console.log(error);
			}
		}
	}
}
</script>