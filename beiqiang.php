# If you want go to  www.love.com,but the firewalld deny you ,so you need change you domain, the first  will transpond  djdj.com  add parameter "search"  explain you domain.
# The second computer, transpond again.  
# The thirdly computer, will point to you new domain.

###     1    ##################################################
[root@a html]# cat first/index.php 

<?php
$the_host = $_SERVER['HTTP_HOST'];
Header("HTTP/1.1 303 Moved Permanently");
Header("refresh:1;url=http://djdj.com/?search=".$the_host);
?>
<html>
<title> 正在跳转官网</title>
<body>
</body>
</html>


###     2    ##################################################
[root@a html]# cat djdj/index.php 
<?php
$hehe = $_GET[ 'search' ];
$he=str_replace("www.","",$hehe);
Header("HTTP/1.1 303 Moved Permanently");
Header("Location: http://7k7k.com/".$he)
?>

###     3    ##################################################
[root@a html]# cat 7k7k/love.com/index.php 
<?php
Header("HTTP/1.1 303 Moved Permanently");
Header("Location: http://www.love.me");
?>

