<h1>File Integrity Monitor</h1>


<h2>Description</h2>
This projects represents the Integrity definition in CIA triad in practical way. With help of Python , simplified FIM application was created.<br/>
Program monitors files in specific folder with checking hashes and amount of files.<br/>
If file was changed,deleted or new file was added - program will alert user.<br/>
Usage guide:<br/>
-Prepare your folder with files and fill files with data you need . After work finished ,run script and choose "Collect new baseline" - this will create unic hashes for your files and write every file name with its hash to separate file.

-After you saved baseline , run program . It will give alerts in real time in case something happenes to your files.

(files in CF2 folder are just example, and program monitor files in this folder , but u can specify your own folder in python script)
<br />
<h2>Languages and modules used</h2>

- <b>Python</b> 
- <b>hashlib,colorama<b>


<h2>Environments Used </h2>

- <b>Windows 10</b>

<h2>Program interface:</h2>


<p align="center">

<h3>Collecting new baseline:<h3>

empty baseline:<br/>
![embl](https://user-images.githubusercontent.com/94048443/216982372-7e6fe37e-bb5c-4fcd-8a72-64ce855e0fa1.png)

Let's fill baseline with hashes and file names:
![blcol](https://user-images.githubusercontent.com/94048443/216982396-67d0222f-78b2-4910-81fa-601a5f050802.png)
<h3>Alerts in real time:<h3>

As long as files are not changed program will be quiet:<br/>
![allgood](https://user-images.githubusercontent.com/94048443/216982440-92bd2f78-810f-4943-a245-4ce987bec14b.png)

Let's change one of files and see what happens: <br/>
![notor](https://user-images.githubusercontent.com/94048443/216982463-f60dd4bf-1448-45c1-b64f-2f3e18574a73.png)<br/>
Program started print alerts.<br/>


Lets see other possible alerts:<br/>
![delbel1](https://user-images.githubusercontent.com/94048443/216982476-169a1f81-7d14-456e-8a78-ad369d94a93e.png)

In conclusion , this simple app will help control an integrity of your files and alert you when some changes in folder occurs

</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
