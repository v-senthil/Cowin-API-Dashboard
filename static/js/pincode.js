var today = new Date();
  var month = new Array();
  month[0] = "01";
  month[1] = "02";
  month[2] = "03";
  month[3] = "04";
  month[4] = "05";
  month[5] = "06";
  month[6] = "07";
  month[7] = "08";
  month[8] = "09";
  month[9] = "10";
  month[10] = "11";
  month[11] = "12";

  var dateno = new Array();
  dateno[1] = "01";
  dateno[2] = "02";
  dateno[3] = "03";
  dateno[4] = "04";
  dateno[5] = "05";
  dateno[6] = "01";
  dateno[7] = "01";
  dateno[8] = "01";
  dateno[9] = "01";
  dateno[10] = "01";
  dateno[11] = "01";
  dateno[12] = "01";
  dateno[13] = "01";
  dateno[14] = "01";
  dateno[15] = "01";
  dateno[16] = "01";
  dateno[17] = "01";
  dateno[18] = "01";
  dateno[19] = "01";
  dateno[20] = "01";
  dateno[21] = "01";
  dateno[22] = "01";
  dateno[23] = "01";
  dateno[24] = "01";
  dateno[25] = "01";
  dateno[26] = "01";
  dateno[27] = "01";
  dateno[28] = "01";
  dateno[29] = "29";
  dateno[30] = "30";
  dateno[31] = "31";


  var date = dateno[today.getDate()]+'-'+month[today.getMonth()]+'-'+today.getFullYear();
  document.getElementById("date").value = date;