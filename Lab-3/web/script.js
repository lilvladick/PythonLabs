fetch('http://localhost:8080/get_data').then(res=> res.json()).then(data=>{
    const dataList = document.getElementById('dataList');
    if (dataList) {
        data.forEach(item => {
          const listItem = document.createElement('li');
          listItem.textContent = `${item.title} - ${item.price}`;
          dataList.appendChild(listItem);
        });
    }
}).catch(err => console.log(err));