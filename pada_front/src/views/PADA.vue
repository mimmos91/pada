<template>
  <!-- upper-->
  <div class="upper">
    <img src="../assets/logo.png" alt="PADA Logo" />

    <div class="profile">
      <!-- <img src="profile.png" alt="Profile" /> -->
      <p>김유경(107032)</p>
    </div>
  </div>
  <div class="containerP">
    <!-- Sidebar -->
    <div class="sidebar">
      <h2>MENU</h2>
      <div class="menu-item">
        <h2>조회 지역선택</h2>
        <label>
          <input
            type="radio"
            name="location"
            value="포항"
            v-model="location"
            @change="logSelection"
          />포항제철소
        </label>
        <br />
        <label>
          <input
            type="radio"
            name="location"
            value="광양"
            v-model="location"
            @change="logSelection"
          />광양제철소
        </label>
      </div>
      <div class="menu-item">
        <h2>지난 데이터</h2>
        <ul>
          <li>2024년 11월 19일</li>
          <li>2024년 11월 7일</li>
          <li>2024년 10월 28일</li>
        </ul>
      </div>
      <button class="button">관리자 메뉴</button>
    </div>

    <!-- Content -->
    <div class="content">
      <!-- Header -->
      <div class="header">
        <h1>Posco Automated Data Analysis</h1>
        <p v-if="location == ''">지역을 선택해 주십시오</p>
        <p v-else-if="location == '포항' || '광양'">
          현재 선택한 지역은 <span style="font-weight: bold">{{ location }} </span>입니다.
        </p>
      </div>

      <!-- Main Content -->
      <div class="main">
        <div class="userChat">
          <div v-if="inquiries.lengh === 0">무엇이든 물어보세요!</div>
          <div v-else>
            <div class="chatContainer" v-for="(items, index) in inquiries" :key="index">
              <div class="speech-bubble">{{ items }}</div>
              <img class="user-icon" src="../assets/user.png" />
            </div>
          </div>
        </div>
      </div>

      <!-- Footer -->
      <div class="footer">
        <input
          type="text"
          v-model="inquiry"
          @keyup.enter="inputInquiry"
          placeholder="무엇을 도와드릴까요?"
        />
        <button class="button" @click="inputInquiry">전송</button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
axios.get()

export default {
  name: 'PADA',
  data() {
    return {
      location: '',
      inquiries: [], // 입력된 값 리스트
      inquiry: '', // 입력된 값
    }
  },
  methods: {
    //라디오 버튼 지역 선택
    logSelection() {
      console.log('지역', this.location)
    },

    //질문 입력 처리
    inputInquiry() {
      if (this.location.trim() == '') {
        alert('지역을 선택해주십시오.')
      } else if (this.inquiry.trim() !== '') {
        console.log('질문:', this.inquiry)
        this.inquiries.push(this.inquiry)
        console.log('리스트에 잘 들어감?', this.inquiries.length)
        this.inquiry = ''
      } else {
        alert('질문을 해 주시기 바랍니다.')
      }
    },
  },
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
  justify-content: space-between;
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
  width: 20%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start center;
  align-content: center;

  background-color: white;
  padding: 10px;
  border: 15px solid #1f497d;
  border-radius: 30px;
  box-sizing: border-box;
  overflow-y: auto;
  overflow-x: hidden;
  margin: 0 10px;
  /* font-size: calc(1rem+0.5vm); */
}

.sidebar div {
  width: 90%;
  font-size: calc(0.8rem + 0.5vw);
}

.sidebar h2 {
  /* font-size: 20px; */
  font-size: calc(0.8rem + 0.3vw);
  margin-top: 10px;
  color: #1f497d;
}

.menu-item {
  margin-bottom: 15px;
}

.menu-item h2 h3 {
  font-size: calc(0.8rem + 0.3vw);
  margin: 0;
  color: #333;
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
  justify-content: center;
}

.footer input {
  flex-grow: 0.8;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;
  box-sizing: border-box;
}

.button {
  padding: 10px 20px;
  background-color: #004b87;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.fixed {
  position: fixed;
  bottom: 0px;
}

.button:hover {
  background-color: #003765;
}
/* 채팅장 스타일 */
.speech-bubble {
  display: flex;
  align-items: center;
  justify-content: right;
  background-color: #2a81b9; /* 파란색 배경 */
  color: white; /* 텍스트 색상 */
  font-size: 14px;
  font-weight: bold;
  padding: 10px 15px;
  border-radius: 10px;
  position: relative;
  width: max-content;
  margin-left: auto;
  margin-bottom: 3px;
}

.speech-bubble:after {
  content: '';
  position: absolute;
  top: 50%;
  right: -10px; /* 말풍선 꼬리의 위치 */
  transform: translateY(-50%);
  border-width: 10px;
  border-style: solid;
  border-color: transparent transparent transparent #2a81b9;
}

.user-icon {
  width: 30px;
  height: 30px;
  background-color: white; /* 아이콘 배경 */
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: 10px;
  color: #2a81b9; /* 아이콘 내부 색 */
  font-size: 16px;
  font-weight: bold;
}

.chatContainer {
  display: flex;
  align-items: center;
}
</style>
