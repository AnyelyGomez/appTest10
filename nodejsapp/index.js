//1. call mysql package
const mysql = require('mysql');
//2. call express package
const express = require('express');
//3. call body-parser package
const bodyparser = require('body-parser');
//4. create a new Express app instance
var app = express();
//5. call JSON request
app.use(bodyparser.json());
//6. create mysql data base connection
var mysqlConnection = mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'',
    database:'market'
});
//7. validate mysql data connection
mysqlConnection.connect((err)=>{
    if(!err)
      console.log('::: Successfull data base connection :::');
    else
      console.log('::: Connection failed :::' + JSON.stringify(err,undefined,2))
})

//8. RUN server
app.listen(3000,()=>console.log('Express server is running at port: 3000:::'));

//9. read all users in data base
app.get('/list_users',(req,res) => {
    mysqlConnection.query('SELECT * FROM users',(err, rows,fields)=>{
        if(!err){
            console.log(rows);
           res.send(rows);
        }else{
        console.log(err);

    }
           
    })

});