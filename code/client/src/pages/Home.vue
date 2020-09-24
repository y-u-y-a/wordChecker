<template>
  <h1>Home Page</h1>
</template>


<script>
export default {

  created() {
    this.allStudents();
    this.getStudent();
  },

  methods: {
    async allStudents() {
      // let url_sample = 'https://qiita.com/api/v2/items?page=1&per_page=20'
      let url = '/api/students/list/';
      let res = await this.axios.get(url);
      let students_list = res.data;
      console.log('一覧：', students_list);
    },
    async getStudent() {
      let url = '/api/students/find/';
      let params = {first_name: 'ああああ'}
      let res = await this.axios.post(url, params);
      let student = res.data;
      console.log('検索：', student);
    }
  }
}
</script>
