fetch('http://localhost:8080/get_data', {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      }
})
.then(res => res.json())
.then(data => {
    const tableBody = document.getElementById('tableBody');
    if (tableBody) {
        data.forEach(item => {
            const tableRow = document.createElement('tr');
            const titleCell = document.createElement('td');
            const descriptionCell = document.createElement('td');
            const priceCell = document.createElement('td');
            const categoryCell = document.createElement('td');
            const sellerContactsCell = document.createElement('td');

            titleCell.textContent = item.title;
            descriptionCell.textContent = item.description;
            priceCell.textContent = item.price;
            categoryCell.textContent = item.category;
            sellerContactsCell.textContent = item.seller_contacts;

            tableRow.appendChild(titleCell);
            tableRow.appendChild(descriptionCell);
            tableRow.appendChild(priceCell);
            tableRow.appendChild(categoryCell);
            tableRow.appendChild(sellerContactsCell);

            tableBody.appendChild(tableRow);
        });
    }
})
.catch(err => console.log(err));



function saveData() {

  const title = document.getElementById('title').value;
  const description = document.getElementById('description').value;
  const price = document.getElementById('price').value;
  const category = document.getElementById('category').value;
  const seller_contacts = document.getElementById('contacts').value;

  const data = {
    title: title,
    description: description,
    price: price,
    category: category,
    seller_contacts: seller_contacts
  };

  fetch('http://localhost:8080/save_data', {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
 .then(res => res.json())
 .then(data => {
   console.log(data);
   alert('Data saved successfully!');
 })
 .catch(err => console.log(err));
  window.location='index.html';
}