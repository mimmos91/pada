<template>
  <!-- upper-->
  <div class="upper">
    <img src="../assets/logo.png" alt="PADA Logo" />
    <p>박현우(162482) / 포스코인재</p>
    <div class="profile">
      <!-- <img src="profile.png" alt="Profile" /> -->
    </div>
  </div>
  <div class="containerP">
    <!-- Sidebar -->
    <div class="sidebar">
      <h2>MENU</h2>
      <div class="menu-item">
        <h3>광양제철소</h3>
      </div>
      <div class="menu-item">
        <h3>포항제철소</h3>
      </div>
      <div class="menu-item">
        <h3>지난 데이터</h3>
        <ul>
          <li>2024년 11월 19일</li>
          <li>2024년 11월 7일</li>
          <li>2024년 10월 28일</li>
        </ul>
      </div>
      <div class="menu-item">
        <h3>관리자 메뉴</h3>
      </div>
    </div>

    <!-- Content -->
    <div class="content">
      <!-- Header -->
      <div class="header">
        <h1>Posco Automated Data Analysis</h1>
      </div>

      <!-- Main Content -->
      <div class="main"></div>

      <!-- Footer -->
      <div class="footer">
        <input type="text" placeholder="입력 중..." />
        <button>전송</button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
axios.get()

export default {
  name: 'PADA',
}
</script>
<style scoped>
body {
  margin: 0 30px;
  font-family: Arial, sans-serif;
  background-color: #f2f4f8;
  padding-left: calc(var(--section-gap) / 2);
}
.upper {
  width: 100%;
  height: 100px;
  text-align: left;
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  margin-bottom: 5px;
  /* display: block; */
}

.upper img {
  height: 100%;
  width: auto;
}
.containerP {
  width: 100%;

  display: flex;
  margin: 0;
  padding: 0;
  flex-direction: row;
  height: 70vh;
  /* padding-right: calc(var(--section-gap) / 2); */
}

.sidebar {
  width: 15%;
  background-color: white;
  padding: 20px;
  border: 15px solid #1f497d;
  border-radius: 30px;
  box-sizing: border-box;
  margin: 0 10px;
}

.sidebar h2 {
  font-size: 20px;
  margin-bottom: 20px;
  color: #333;
}

.menu-item {
  margin-bottom: 15px;
}

.menu-item h3 {
  font-size: 16px;
  margin: 0;
  color: #1f497d;
  cursor: pointer;
}

.menu-item ul {
  list-style: none;
  padding-left: 20px;
  margin: 5px 0 10px 0;
}

.menu-item ul li {
  font-size: 14px;
  color: #555;
}

.content {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  background-color: #fff;
  border: 1px solid #004b87;
  border-radius: 30px;
  max-width: 1280px;
}

.header {
  background-color: #004b87;
  color: #fff;
  padding: 15px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top-left-radius: 30px;
  border-top-right-radius: 30px;
}

.header h1 {
  font-size: 18px;
  margin: 0;
}

.header .profile {
  font-size: 14px;
  display: flex;
  align-items: center;
}

.header .profile img {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 10px;
}

.main {
  flex-grow: 1;
  padding: 20px;
  box-sizing: border-box;
}

.footer {
  border-top: 1px solid #ccc;
  padding: 10px 20px;
  display: flex;
  align-items: center;
}

.footer input {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;
  box-sizing: border-box;
}

.footer button {
  padding: 10px 20px;
  background-color: #004b87;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.footer button:hover {
  background-color: #003765;
}
</style>
