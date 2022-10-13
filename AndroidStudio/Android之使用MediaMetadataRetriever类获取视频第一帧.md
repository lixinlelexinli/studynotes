https://blog.csdn.net/u012561176/article/details/47858099

# Android之使用MediaMetadataRetriever类获取视频第一帧



![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5CAndroidStudio%5CUntitled.assets%5Coriginal.png)

[茕夜](https://blog.csdn.net/u012561176) 2015-08-22 12:32:07 ![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5CAndroidStudio%5CUntitled.assets%5CarticleReadEyes.png) 20726 ![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5CAndroidStudio%5CUntitled.assets%5CtobarCollect.png) 收藏 4

分类专栏： [Android多媒体应用](https://blog.csdn.net/u012561176/category_2922053.html) 文章标签： [android](https://www.csdn.net/tags/MtTakg2sNjM0Ni1ibG9n.html) [获取视频第一帧](https://so.csdn.net/so/search/s.do?q=获取视频第一帧&t=blog&o=vip&s=&l=&f=&viparticle=)

版权

一.首先，来介绍一下MediaMetadataRetriever类，此类位于android.media包下，这里，先附上可查看此类的API地址：[MediaMetadataRetriever类](http://android.toolib.net/reference/android/media/MediaMetadataRetriever.html)，大家可以自行查看。

1.MediaMetadataRetriever类概述：MediaMetadataRetriever class provides a unified interface for retrieving frame and meta data from an input media file.

翻译过来是Mediametadataretriever类提供了一个统一的接口取回帧和取回从一个输入媒体文件中的元数据。

2.MediaMetadataRetriever类提供的常量：MediaMetadataRetriever类提供的常量有很多，都是int常量，有些用来取得媒体文件的元数据，有些用来对获得视频的帧的操作，这里大家可以查看API，这里列举几个常量：

![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5CAndroidStudio%5CUntitled.assets%5C20150822115108561)

第一个是获得我们设置的媒体文件的专辑标题，第二个是获得我们设置的媒体文件的专辑艺术家，第三个获得我们设置的媒体文件的艺术家，第四个获得我们设置的媒体文件的作者。

3.MediaMetadataRetriever类的构造方法：MediaMetadataRetriever() 无参构造方法。

4.MediaMetadataRetriever类的公有方法，如下图所示：

![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5CAndroidStudio%5CUntitled.assets%5C20150822115646732)

大家可以根据解释来知道这些方法的用处，其中一常用的方法为setDataSource方法，用来设置数据源，其中这个数据源可以从文件的路径，文件描述符，uri地址和Uri对象来设置。另外一常用的方法getFrameAtTime方法，用来获取帧，返回一个Bitmap对象，其中可以获取到第一帧和多少时间后的帧。





二.此篇文章主要是介绍如何使用MediaMetadataRetriever类获取视频第一帧的，在编写我们的Android项目之前，还是要做以下三个步骤：

1.开启Android模拟器。

2.打开视图File Explorer，即展示Android模拟器中文件目录和文件，其中，必须注意的是Android模拟器的版本问题，版本不同存放在SD卡的位置也不同，Android2.x系统SD卡存放的位置为/mnt/sdcard或者/sdcard，而Android4.x系统SD卡存放的位置为/storage/sdcard/。

3.接着就把我们的视频文件放入SD卡的位置上，我的模拟器版本为4.x的，所以就在下图的位置存放视频文件：

![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5CAndroidStudio%5CUntitled.assets%5C20150822121324653)

如果你存放的文件目录是没有权限放入文件的，就会在控制台输出红色警告，没有权限。





三.下面，就可以编写我们的Android项目，新建一个项目android_mediaMetadataRetriever：

1.打开我们的布局文件activity_main.xml，代码如下：

```xml
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"



    xmlns:tools="http://schemas.android.com/tools"



    android:layout_width="match_parent"



    android:layout_height="match_parent"



    android:orientation="vertical" >

    <ImageView 

        android:id="@+id/imageView"



        android:layout_width="wrap_content"



        android:layout_height="wrap_content"



        android:layout_gravity="center"



        android:src="@drawable/ic_launcher"/>



    



    <Button 



        android:id="@+id/button"



        android:layout_width="match_parent"



        android:layout_height="wrap_content"



        android:text="获取视频缩略图"/>

</LinearLayout>
```

2.打开我们的MainActivity.java文件，代码如下：

```html
package com.android_mediametadataretriever;



 



import java.io.File;



 



import android.app.Activity;



import android.graphics.Bitmap;



import android.media.MediaMetadataRetriever;



import android.os.Bundle;



import android.view.View;



import android.view.View.OnClickListener;



import android.widget.Button;



import android.widget.ImageView;



import android.widget.Toast;



 



public class MainActivity extends Activity {



 



	private ImageView imageView;//声明ImageView对象



	private Button button;//声明Button对象



	@Override



	protected void onCreate(Bundle savedInstanceState) {



		super.onCreate(savedInstanceState);



		setContentView(R.layout.activity_main);



		imageView=(ImageView)findViewById(R.id.imageView);//获取布局管理器中的ImageView控件



		button=(Button)findViewById(R.id.button);//获取布局管理器中的Button控件



		//设置按钮点击事件监听器



		button.setOnClickListener(new OnClickListener() {



			



			@Override



			public void onClick(View v) {



				MediaMetadataRetriever mmr=new MediaMetadataRetriever();//实例化MediaMetadataRetriever对象



				File file=new File("/storage/sdcard/Movies/music1.mp4");//实例化File对象，文件路径为/storage/sdcard/Movies/music1.mp4



				if(file.exists()){



					mmr.setDataSource(file.getAbsolutePath());//设置数据源为该文件对象指定的绝对路径



					Bitmap bitmap=mmr.getFrameAtTime();//获得视频第一帧的Bitmap对象



					if(bitmap!=null){



						imageView.setImageBitmap(bitmap);//设置ImageView显示的图片



						Toast.makeText(MainActivity.this, "获取视频缩略图成功", Toast.LENGTH_SHORT).show();//获取视频缩略图成功，弹出消息提示框



					}else{



						Toast.makeText(MainActivity.this, "获取视频缩略图失败", Toast.LENGTH_SHORT).show();//获取视频缩略图失败，弹出消息提示框



					}



				}else{



					Toast.makeText(MainActivity.this, "文件不存在", Toast.LENGTH_SHORT).show();//文件不存在时，弹出消息提示框



				}



			}



		});



	}



 



}
```

其中上面代码中的File对象指定的路径为Android 4.x系统的SD卡路径下的目录，如果是较低版本，还是要看下File Explorer视图的SD卡路径是哪个，其中/mnt/sdcard目录和/sdcard目录都属于/storage/sdcard目录的连接文件，所以真实存放路径为/storage/sdcard。

3.最后，千万记得一点，要在AndroidManifest.xml声明文件添加我们的许可，即权限，在此文件加上一行读取SD卡文件的权限代码即可，代码如下：

```html
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

注：其中必须注意的是使用MediaMetadataRetriever类要求android的minSdkVersion最小为14，所以如果你的AndroidManifest.xml文件中的android:minSDKVersion="8"即最小的sdk版本小于14的话，将会报错，解决办法可以在AndroidManifest.xml文件中改最小sdk版本，也可以在MainActivity类中加上下面的代码：

```html
@TargetApi(Build.VERSION_CODES.ICE_CREAM_SANDWICH)
```

使得我们使用这个MediaMetadataRetriever类不会报错。



四.部署此项目到Android模拟器，运行效果如下：

![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5CAndroidStudio%5CUntitled.assets%5C20150822122858465)

点击获取视频缩略图按钮，如下图所示：

![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5CAndroidStudio%5CUntitled.assets%5C20150822122943086)





五.以上内容仅供大家学习参考，写得不好，请见谅，如有错误，请指出，谢谢！