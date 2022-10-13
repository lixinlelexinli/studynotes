# SharedPreferences

# 快捷键

| shift+F10   | 运行当前模块           |
| ----------- | ---------------------- |
| ctrl + F5   | 清理并重新运行当前模块 |
| alt + enter | 导入包                 |
| shift + F6  | 重命名                 |

# 屏幕显示

dp字体大小不随系统设置改变，sp字体大小随系统改变，sp用于字体大小，其他尺寸大小用dp

## 颜色

![image-20210118110026664](F:%5Cgithub%5Cgithubio%5Cstudynotes%5CAndroidStudio%5CAndroidStudio.assets%5Cimage-20210118110026664.png)

![image-20210118110117622](F:%5Cgithub%5Cgithubio%5Cstudynotes%5CAndroidStudio%5CAndroidStudio.assets%5Cimage-20210118110117622.png)

## 简单布局

![image-20210118111443881](F:%5Cgithub%5Cgithubio%5Cstudynotes%5CAndroidStudio%5CAndroidStudio.assets%5Cimage-20210118111443881.png)

### LinearLayout

* orientation 指定方向，horizontal水平方向，vertical垂直方向

* gravity ： 指定内部视图与本线性布局的对齐方向

  在代码中增加

  * setOrientation:LinearLayout.HORIZONTAL水平布局，LinearLayout.VERTICAL垂直布局

### ScrollView

1. 水平滚动 HorizontalScrollView，width：match_parent，height：wrap_content
2. 垂直滚动 ScrollView，height：match_parent，width：wrap_content，fillViewPort="true"填满试图窗口

# 中级控件

## FrameLayout

一般用于需要重叠显示的场合

## 特殊按钮

### 复选框 CheckBox

CompoundButton属性：checked勾选状态，默认false，button指定左侧勾选图形的图形

在代码中设置setChecked设置勾选状态，setButtonDrawable设置勾选图形，setOnCheckedChangeListener：设置勾选状态变换的监听器，isChecked：判断按钮是否勾选。

# NoScrollGridView

# 不可滑动的 Gridview（NoScrollGridView）

![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5CAndroidStudio%5CAndroidStudio.assets%5Coriginal.png)

> 不可滑动的 Gridview，用于 scrollview 中嵌套 gridview 等多种布局展示数据时，解决滑动冲突问题

去除 gridview 滑动到尽头时的阴影效果

> android:overScrollMode=“never”

```java
public class NoScrollGridView extends GridView {

    public NoScrollGridView(Context context, AttributeSet attrs) {
        super(context, attrs);
    }

    public NoScrollGridView(Context context) {
        super(context);
    }

    public NoScrollGridView(Context context, AttributeSet attrs, int defStyle) {
        super(context, attrs, defStyle);
    }

    /**
     * 设置gridView不可滑动
     * @param widthMeasureSpec
     * @param heightMeasureSpec
     */
    @Override
    public void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {
        int expandSpec = MeasureSpec.makeMeasureSpec(
                Integer.MAX_VALUE >> 2, MeasureSpec.AT_MOST);
        super.onMeasure(widthMeasureSpec, expandSpec);
    }
}
```

# 开源代码

## ANDROID的实现既能相册选择，拍照选择，点击每张图片又能放大查看！

标签： [X相册](https://www.freesion.com/tag/X相册/) [p拍照](https://www.freesion.com/tag/p拍照/) [图片放大](https://www.freesion.com/tag/图片放大/)

#### 最近很长一段时间没有更新博客了实在是比较忙最近需要使用一个功能：选择本机相册或者拍照返回图片显示到九宫格中，并且可以点击九宫格每一张放大查看，滑动等功能！

在网上也看到一些大神写的演示和第三方库，不过发现很多都不完整，有的只是实现相册选择，没有实现拍照功能;有的实现了相册和拍照功能又没有实现点击放大查看滑动功能;所以我就跟据那些演示完善了一下，实现既能相册选择，拍照选择，点击每张图片又能放大查看现在来看看怎么实现的！

来看看效果图吧！

![img](https://www.freesion.com/images/94/ddb6ddede56266e1b3e40c2483b790a6.png)

image.png

![img](https://www.freesion.com/images/344/d48d0e2b25e8a58d156301662f182288.png)

image.png

![img](https://www.freesion.com/images/210/82b5c057fc78f0d63d9cb5fe79da9a4a.png)

image.png

使用到的依赖库是

```
compile 'me.iwf.photopicker:PhotoPicker:0.1.8'
```

来看看首页的布局：activity_main.xml中中

```
<?xml version="1.0" encoding="utf-8"?>



<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"



    xmlns:app="http://schemas.android.com/apk/res-auto"



    xmlns:tools="http://schemas.android.com/tools"



    android:layout_width="match_parent"



    android:layout_height="match_parent"



    android:orientation="vertical"



    tools:context="com.an.myphotodemo.MainActivity">



 



  



 



 



    <com.an.myphotodemo.NoScrollGridView



        android:layout_width="match_parent"



        android:layout_height="wrap_content"



        android:layout_below="@+id/view_gad"



        android:layout_marginBottom="10dp"



        android:layout_marginLeft="3dp"



        android:layout_marginRight="3dp"



        android:layout_marginTop="3dp"



        android:numColumns="3"



 



        android:scrollbars="none"



        android:verticalSpacing="3dp"



        android:id="@+id/recycler_view"/>



 



 



</LinearLayout>



 
```

##### NOSCROLLGRIDVIEW是自定义的一个SCROLLGRIDVIEW

```java
public class NoScrollGridView extends GridView {



    public NoScrollGridView(Context context, AttributeSet attrs) {



        super(context, attrs);



    }



    public NoScrollGridView(Context context) {



        super(context);



    }



    public NoScrollGridView(Context context, AttributeSet attrs, int defStyle) {



        super(context, attrs, defStyle);



    }



    @Override



    public void onMeasure(int widthMeasureSpec, int heightMeasureSpec) {



        int expandSpec = MeasureSpec.makeMeasureSpec(



                Integer.MAX_VALUE >> 2, MeasureSpec.AT_MOST);



        super.onMeasure(widthMeasureSpec, expandSpec);



    }



}
```

对了，还需要一些工具类，后面再说，现在来看看主要实现的代码！

首页的OnCreate中（）中NoScrollGridView初始化并且设置适配器

```java
 @Override



    protected void onCreate(Bundle savedInstanceState) {



        super.onCreate(savedInstanceState);



        setContentView(R.layout.activity_main);



        itemLayout = (NoScrollGridView) findViewById(R.id.recycler_view);



 



        ninePicturesAdapter = new NinePicturesAdapter(this, 9, new NinePicturesAdapter.OnClickAddListener() {



            @Override



            public void onClickAdd(int positin) {



                choosePhoto();



            }



        }, new NinePicturesAdapter.OnItemClickAddListener() {



            @Override



            public void onItemClick(int positin) {



 



                Log.i(TAG, "-------------onItemClick: "+positin);



 



                String[] array = new String[ninePicturesAdapter.getPhotoCount()];



                // List转换成数组



                for (int i = 0; i < photossss.size()-1; i++) {



                    array[i] = photossss.get(i);



                }



                //数组转换为集合



                //List<String> stringsss = Arrays.asList(array);



 



                Log.i(TAG, "----array:--- "+array.length);



                imageBrower(positin,array);



            }



        });



        itemLayout.setAdapter(ninePicturesAdapter);



 



    }
```

/ ** 
*开启图片选择器choosePhoto（）
\* /

```cpp
    private void choosePhoto() {



        PhotoPickerIntent intent = new PhotoPickerIntent(MainActivity.this);



        intent.setPhotoCount(9);



        intent.setShowCamera(true);



        startActivityForResult(intent, REQUEST_CODE);



 



        //ImageLoaderUtils.display(context,imageView,path);



    }
```

/ ** 
*每一张图片放大查看
\* @param position 
\* @param网址
\* /

```cpp
    private void imageBrower(int position, String[] urls) {



        Intent intent = new Intent(this, ImagePagerActivity.class);



        // 图片url,为了演示这里使用常量，一般从数据库中或网络中获取



        intent.putExtra(ImagePagerActivity.EXTRA_IMAGE_URLS, urls);



        intent.putExtra(ImagePagerActivity.EXTRA_IMAGE_INDEX, position);



        startActivity(intent);



    }



 
```

/ ** 
*接受返回的图片数据：onActivityResult（）
\* @param requestCode 
\* @param resultCode 
\* @param data 
\* /

```java
@Override protected void onActivityResult(int requestCode, int resultCode, Intent data) {



        super.onActivityResult(requestCode, resultCode, data);



 



        if (resultCode == RESULT_OK && requestCode == REQUEST_CODE) {



            if (data != null) {



                photos = data.getStringArrayListExtra(PhotoPickerActivity.KEY_SELECTED_PHOTOS);



 



                for (int i = 0; i < photos.size(); i++) {



                    Log.i(TAG, "----------onActivityResult: "+ photos.get(i));



                }



                    if(ninePicturesAdapter!=null) {



                        Log.i(TAG, "----------photossss: ========");



                        ninePicturesAdapter.addAll(photos);



          



                      //获取九宫格显示的所有图片数据



                        photossss = ninePicturesAdapter.getData();



                        Log.i(TAG, "----------photossss: ========"+photossss.size());



                        



                    }



            }



        }



    }
```

到这里主页代码已经完成了，现在来看看适配器是如何完成的NinePicturesAdapter 
/ **

- DES：9宫图适配器
- 由一个创建
- 于2016.09.16：33 
  \* /

```java
public class NinePicturesAdapter extends BaseAblistViewAdapter<String> {



    private boolean showAdd = true;



    private int picturnNum = 0;



    private boolean isDelete = false;//当前是否显示删除按钮



    private OnClickAddListener onClickAddListener;



    private OnItemClickAddListener onItemClickListener;



    private boolean isAdd=true;//当前是否显示添加按钮

    private static final String TAG = "NinePicturesAdapter";



    public NinePicturesAdapter(Context context, int picturnNum, OnClickAddListener onClickAddListener,OnItemClickAddListener onItemClickListener) {
    super(context);
        this.picturnNum = picturnNum;



        this.onClickAddListener = onClickAddListener;



        this.onItemClickListener=onItemClickListener;



        showAdd();



    }

    @Override
    public View getView(final int position, View convertView, ViewGroup parent) {



        if (convertView == null) {



            convertView = LayoutInflater.from(mContext).inflate(R.layout.item_grid_photo, parent, false);



        }



        final ImageView imageView = ViewHolderUtil.get(convertView, R.id.img_photo);



        ImageView imgDelete = ViewHolderUtil.get(convertView, R.id.img_delete);



        final String url = getData().get(position);



        //显示图片



        if (TextUtils.isEmpty(url) && showAdd) {



            ImageLoaderUtils.display(mContext, imageView, R.drawable.addphoto);



            imgDelete.setVisibility(View.GONE);



        } else {



            imgDelete.setVisibility(View.VISIBLE);



            ImageLoaderUtils.display(mContext, imageView, url);



        }



 



        autoHideShowAdd();



 



        imageView.setOnClickListener(new View.OnClickListener() {



            @Override



            public void onClick(View view) {



                //再次选择图片



                if (TextUtils.isEmpty(url)) {



                    if (onClickAddListener != null) {



                        onClickAddListener.onClickAdd(position);



                    }



                } else {



                    //放大查看图片



 



                    onItemClickListener.onItemClick(position);



                    Log.i(TAG, "onClick: "+position);



                    //BigImagePagerActivity.startImagePagerActivity((Activity) mContext, getData(), position);



                }



            }



        });



        //删除按钮



        imgDelete.setOnClickListener(new View.OnClickListener() {



            @Override



            public void onClick(View view) {



                remove(position);



                if (!isDelete && getCount() < 1) {



                    add("");



                    isDelete = true;



                }



                notifyDataSetChanged();



            }



        });



        return convertView;



    }



 



    @Override



    public void setData(List<String> d) {



        boolean hasAdd=false;



        for (int i = 0; i < d.size(); i++) {



            if(TextUtils.isEmpty(d.get(i))){



                hasAdd=true;



                break;



            }



        }



        super.setData(d);



        if(!hasAdd){



            showAdd();



        }



    }



 



    @Override



    public void addAll(List<String> d) {



        if(isAdd){



            HideAdd();



        }



        super.addAll(d);



        showAdd();



    }



 



    /**



     * 移除add按钮



     */



    public void autoHideShowAdd(){



        int lastPosition=getData().size()-1;



            if(lastPosition==picturnNum&&getData().get(lastPosition)!=null&& TextUtils.isEmpty(getData().get(lastPosition))){



                getData().remove(lastPosition);



                isAdd=false;



                notifyDataSetChanged();



            }else if(!isAdd){



                showAdd();



            }



    }



    /**



     * 移除add按钮



     */



    public void HideAdd(){



        int lastPosition=getData().size()-1;



        if(getData().get(lastPosition)!=null&& TextUtils.isEmpty(getData().get(lastPosition))){



            getData().remove(lastPosition);



            isAdd=false;



            notifyDataSetChanged();



        }



    }



    /**



     * 显示add按钮



     */



    public void showAdd(){



        if(getData().size()<picturnNum){



 



 



 



            addAt(getData().size(),"");



            isAdd=true;



            notifyDataSetChanged();



        }



    }



 



    /**



     * 获取图片张数



     * @return



     */



   public int getPhotoCount(){



       return isAdd==true?getCount()-1:getCount();



   }



 



 



    /**



     * 加号接口



     */



    public interface OnClickAddListener {



        void onClickAdd(int positin);



    }



 



    public interface OnItemClickAddListener {



        void onItemClick(int positin);



    }



 



}
```

适配器加载的布局如下

```
<?xml version="1.0" encoding="utf-8"?>



<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"



    android:layout_width="match_parent"



    android:layout_height="match_parent"



    android:background="@android:color/white"



    android:layout_centerInParent="true"



    android:layout_gravity="center"



    android:gravity="center"



    android:orientation="vertical">



    <RelativeLayout



        android:id="@+id/rr_gad"



        android:layout_width="wrap_content"



        android:layout_height="wrap_content"



        android:padding="5dp">



 



        <ImageView



            android:id="@+id/img_photo"



            android:layout_width="80dp"



            android:layout_height="80dp"



            android:scaleType="centerCrop" />



 



    </RelativeLayout>



    <ImageView



        android:id="@+id/img_delete"



        android:layout_width="30dp"



        android:layout_height="30dp"



        android:layout_alignRight="@+id/rr_gad"



        android:layout_alignTop="@+id/rr_gad"



        android:background="@drawable/cha" />



</RelativeLayout>
```

ImageLoaderUtils是一个图片加载显示的工具类，当然也可以使用其他的

至此：相册选择和拍照功能，显示九宫图皆以实现，现在来看看图片放大查看：布局如下image_detail_pager.xml

```
<?xml version="1.0" encoding="utf-8"?>



<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"



    android:layout_width="match_parent"



    android:layout_height="match_parent" >



 



    <com.an.myphotodemo.image.HackyViewPager



        android:id="@+id/pager"



        android:layout_width="match_parent"



        android:layout_height="match_parent"



        />



 



    <TextView



        android:id="@+id/indicator"



        android:layout_width="match_parent"



        android:layout_height="wrap_content"



        android:layout_gravity="bottom"



        android:gravity="center"



        android:textSize="18sp"



        android:textColor="@android:color/white"



        android:text="@string/viewpager_indicator"



        android:background="@android:color/transparent" />



 



</FrameLayout>



 
```

查看图片滑动主业如下：

```java
public class ImagePagerActivity extends FragmentActivity {



    private static final String STATE_POSITION = "STATE_POSITION";



    public static final String EXTRA_IMAGE_INDEX = "image_index";



    public static final String EXTRA_IMAGE_URLS = "image_urls";



 



    private HackyViewPager mPager;



    private int pagerPosition;



    private TextView indicator;



 



    private static final String TAG = "ImagePagerActivity";



    @Override



    public void onCreate(Bundle savedInstanceState) {



        super.onCreate(savedInstanceState);



        setContentView(R.layout.image_detail_pager);



 



        pagerPosition = getIntent().getIntExtra(EXTRA_IMAGE_INDEX, 0);



        String[] urls = getIntent().getStringArrayExtra(EXTRA_IMAGE_URLS);



 



        Log.i(TAG, "length: "+urls.length);



 



 



        mPager = (HackyViewPager) findViewById(R.id.pager);



        ImagePagerAdapter mAdapter = new ImagePagerAdapter(



                getSupportFragmentManager(), urls);



        mPager.setAdapter(mAdapter);



        indicator = (TextView) findViewById(R.id.indicator);



 



        CharSequence text = getString(R.string.viewpager_indicator, 1, mPager



                .getAdapter().getCount());



        indicator.setText(text);



        // 更新下标



        mPager.setOnPageChangeListener(new OnPageChangeListener() {



 



            @Override



            public void onPageScrollStateChanged(int arg0) {



            }



 



            @Override



            public void onPageScrolled(int arg0, float arg1, int arg2) {



            }



 



            @Override



            public void onPageSelected(int arg0) {



                CharSequence text = getString(R.string.viewpager_indicator,



                        arg0 + 1, mPager.getAdapter().getCount());



                indicator.setText(text);



            }



 



        });



        if (savedInstanceState != null) {



            pagerPosition = savedInstanceState.getInt(STATE_POSITION);



        }



 



        mPager.setCurrentItem(pagerPosition);



    }



 



    @Override



    public void onSaveInstanceState(Bundle outState) {



        outState.putInt(STATE_POSITION, mPager.getCurrentItem());



    }



 



    private class ImagePagerAdapter extends FragmentStatePagerAdapter {



 



        public String[] fileList;



 



        public ImagePagerAdapter(FragmentManager fm, String[] fileList) {



            super(fm);



            this.fileList = fileList;



        }



 



        @Override



        public int getCount() {



            return fileList == null ? 0 : fileList.length;



        }



 



        @Override



        public Fragment getItem(int position) {



            String url = fileList[position];



            return ImageDetailFragment.newInstance(url);



        }



 



    }



}
```

这里就结束了，想了解更多的点这里：[https](https://link.jianshu.com/?t=https://github.com/caichengan/MyPhotoDemo)：
[//github.com/caichengan/MyPhotoDemo](https://link.jianshu.com/?t=https://github.com/caichengan/MyPhotoDemo)

版权声明：本文为an13531829360原创文章，遵循[ CC 4.0 BY-SA ](https://creativecommons.org/licenses/by-sa/4.0/)版权协议，转载请附上原文出处链接和本声明。本文链接：https://blog.csdn.net/an13531829360/article/details/80535386

[![img](F:%5Cgithub%5Cgithubio%5Cstudynotes%5CAndroidStudio%5CAndroidStudio.assets%5Clogo.jpg)](https://www.freesion.com/)

## 灰信网（软件开发博客聚合）

程序员专属的优秀博客文章阅读平台

- ### [ANDROID 拍照或相册中选择图片编辑功能（仿微信拍照或相册选择照片编辑功能）](https://www.freesion.com/article/8292164402/)

- ### [ANDROID 头像选择(拍照、相册裁剪),含7.0的坑](https://www.freesion.com/article/3823989973/)

- ### [ANDROID获取相册图片-实现选择相册图片功能](https://www.freesion.com/article/7189488464/)

- ### [ANDROID 中拍照、相册选择、裁剪照片](https://www.freesion.com/article/74161248234/)

- ### [ANDROID WEBVIEW 选择图片并上传（调用相机拍照/相册/选择文件）](https://www.freesion.com/article/72001147857/)

- ### [ANDROID7.0调用系统相机拍照、相册选择图片、裁剪 图片压缩](https://www.freesion.com/article/7577653804/)

- ### [解决ANTD SELECT支持既能输入不存在的选项又能进行下拉框选择](https://www.freesion.com/article/3239744770/)

- ### [ANDROID WEBVIEW实现选择本地图片拍照功能](https://www.freesion.com/article/9960209496/)

- ### [ANDROID 实现拍照,选择图片并剪切保存](https://www.freesion.com/article/58861103030/)

COPYRIGHT © 2010-2021 - ALL RIGHTS RESERVED - [WWW.FREESION.COM](https://www.freesion.com/)



## 其他仿朋友圈照片内容

https://github.com/yexseven/EasyPhotos

https://blog.csdn.net/stephen2wong/article/details/68921740

https://www.jianshu.com/p/0027ec2c5654

https://www.jb51.net/article/158640.htm

https://www.jb51.net/article/123547.htm



# 从imageview Android中移除图像

### 热门回答

```java
imageView.setImageDrawable(null);
```

### 2 

setVisibility(View.GONE)`or`setVisibility(View.INVISIBLE)`对我不起作用，因为当看不见/消失时我停止了46648924检测(并且用户被锁定到当前图像)。

# 签名发布

## 签名文件

在进行打包之前，首先需要一个签名文件。

> eclipse的签名文件是以.ketstore为后缀的文件；Android Studio是以.jks为后缀的文件。

签名文件有几个要素

|     英文名称      |     解释     |
| :---------------: | :----------: |
|     keyStore      |  密钥库路径  |
| keyStore Password |  密钥库密码  |
|     keyAlias      | 签名文件别名 |
|    keyPassword    | 签名文件密码 |

### 默认签名文件

在开发阶段，用到第三方SDK新建应用项目时，需要签名KEY的SHA1。这里可以使用Android Studio自带的debug.keystore。

可以使用命令`keytool -list -v -keystore ~/.android/debug.keystore -alias androiddebugkey -storepass android -keypass android`在终端中直接获取到签名key的SHA1信息，如下图:

![img](https:////upload-images.jianshu.io/upload_images/1311456-aefaf940d952be38.png?imageMogr2/auto-orient/strip|imageView2/2/w/804/format/webp)

Android Studio默认key.png

> `~`代表的是账户的根目录

对应要素:

|     要素名称      |            值             |
| :---------------: | :-----------------------: |
|     keystore      | ~/.android/debug.keystore |
| keyStore password |          android          |
|     keyAlias      |      androiddebugkey      |
|    keyPassword    |          android          |

> 默认路径下的debug.keystore不存在时，会自动创建。如果修改了debug.keystore路径，并不会在新路径下自动创建debug.keystore文件。如果在默认路径创建一个不以debug命名的key，系统还是会自动创建该签名文件。所以只有使用默认路径，才会自动创建相应的key文件

**参考**

[Android Studio获取调试包签名的SHA1值方法](https://link.jianshu.com?t=http://www.yuochong.com/139.html)，[signing configurations（签名配置）](https://link.jianshu.com?t=https://avatarqing.github.io/Gradle-Plugin-User-Guide-Chinese-Verision/basic_project/signing_configurations.html)

### 创建签名文件生成Apk文件

通过Build->Generate Signed APK，选择module然后next，点击creat new...选项创建一个新的key文件。如下图填写一些基本信息

![img](https:////upload-images.jianshu.io/upload_images/1311456-e432a46d64f97c86.png?imageMogr2/auto-orient/strip|imageView2/2/w/521/format/webp)

签名信息.png

|        名称         |    描述    |
| :-----------------: | :--------: |
|   key store path    | 密钥库路径 |
|      password       | 密钥库密码 |
|       confirm       |  确认密码  |
|        alias        |    别名    |
|      validity       |  有效年限  |
| first and last name |    名字    |
|  organization unit  | 公司或组织 |
|    organization     |    公司    |
|  city or locality   |     省     |
|  state or province  |   市或洲   |
|    country code     |  国家代码  |

然后点击next->选择Build Type->Finish。此时Apk文件就生成了，同时签名文件也生成在相应目录。
 这里注意到，`已经利用了Build->Generate Signed APK打包了Apk`。

[云社区](https://bbs.huaweicloud.com/) [博客](https://bbs.huaweicloud.com/blogs) 博客详情

# 关于Android studio签名打包Warning：jks密钥库使用专用格式…

[![img](https://bbs-img.huaweicloud.com/user/img/head/1601435619333_2015_1299.png)](https://bbs.huaweicloud.com/community/usersnew/id_1554886269182568) *[CSDN](https://bbs.huaweicloud.com/community/usersnew/id_1554886269182568)* 发表于 2020-11-14 22:25:21

 80 

 0 

 0

[Android](https://developer.huaweicloud.com/tags/200636/blog_1)[Android Studio](https://developer.huaweicloud.com/tags/200762/blog_1)

【摘要】 ** 关于Android studio打包Warning：jks… ** 这里点击OK，然后在Android studio的Terminal 中把上图标红的部分复制下来， C:\Users\Administrator\Desktop\aip-ocr-android-sdk-1.4.4\laughing>keytool -importkeystore -srck...

**

# 关于Android studio打包Warning：jks…

**

![android studio自带的打包工具签名的时候会提示警告：迁移到行业标准格式PKCS12](https://img-blog.csdnimg.cn/20201111114116958.png#pic_center)
这里点击OK，然后在Android studio的Terminal
中把上图标红的部分复制下来，

```javascript
C:\Users\Administrator\Desktop\aip-ocr-android-sdk-1.4.4\laughing>keytool -importkeystore -srckeystore C:\Users\Administrator\Desktop\testjks\test.jks -destkeystore C:\Users\Administrator\Desktop\testjks\test.jks -deststoretype pkcs12
```

粘贴到里边，然后如果直接复制粘贴的话，会出现

![在这里插入图片描述](https://img-blog.csdnimg.cn/202011111143593.png#pic_center)
**

```javascript
keytool 错误: java.io.IOException: DerInputStream.getLength(): lengthTag=109, too big.**
```

这里就需要把后边的那个jks的文件名修改一下，例如我的就是把test.jks改成了test1.jks,然后就通过了
然后：keytool -list -v -keystore (路径).jks就可以查询签名的一些MD5 SHA1等乱七八杂的信息了

## 今天对AS新项目打包的时候突然出现了一个错误

![img](https://www.pianshen.com/images/498/bf3fd53cb2edd64668ca825e5dde1182.png)

### 解决办法：

![img](https://www.pianshen.com/images/199/a83e84ff5733f6cd97318d3593fcd2af.png)

### 1.把这句话复制下来，在你的cmd窗口里复制这句话，运行输入你的秘钥口令

![img](https://www.pianshen.com/images/270/0d0caeaa7f5eda99d389b147f2c6e266.png)

### 2.运行完之后我们的AS正常打包，（有的正常了，有的小伙伴在打包最后一步finish的有时候会报错）



https://www.cnblogs.com/definedone/p/11586487.html

https://square.github.io/okhttp/

# 内存读取

https://www.jb51.net/article/88596.htm

# 系统信息

https://www.jb51.net/article/36650.htm

https://www.jb51.net/article/73764.htm

https://zhuanlan.zhihu.com/p/261701953

# APP信息

https://www.jianshu.com/p/923a3367b62e

https://www.jianshu.com/p/0fba8fd4a1e2

https://blog.csdn.net/q384415054/article/details/72972405/

https://blog.csdn.net/u012246458/article/details/89350354?utm_medium=distribute.pc_relevant_download.none-task-blog-BlogCommendFromBaidu-7.nonecase&dist_request_id=1328270.150.16155078842322185&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-BlogCommendFromBaidu-7.nonecas

点击跳转https://blog.csdn.net/qq_40315080/article/details/96853966?utm_medium=distribute.pc_relevant_download.none-task-blog-baidujs-6.nonecase&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-baidujs-6.nonecase

https://blog.csdn.net/qq_43616001/article/details/104242694?utm_medium=distribute.pc_relevant_download.none-task-blog-BlogCommendFromBaidu-8.nonecase&dist_request_id=1328270.150.16155078842322185&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-BlogCommendFromBaidu-8.nonecas

## 是否安装某应用

https://blog.csdn.net/yufumatou/article/details/101277235

## 权限

https://blog.csdn.net/kefanpipi/article/details/9000984?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-9.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-9.control

https://blog.csdn.net/lknlll/article/details/76242255?utm_term=androidapp%E6%9D%83%E9%99%90%E6%A3%80%E6%B5%8B&utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~sobaiduweb~default-0-76242255&spm=3001.4430

https://blog.csdn.net/qq_25066049/article/details/83410076

## 运行时签名校验

https://www.jianshu.com/p/50f2a8db2ab0

## 获取应用使用情况

https://www.jianshu.com/p/f88b6a9f7462

