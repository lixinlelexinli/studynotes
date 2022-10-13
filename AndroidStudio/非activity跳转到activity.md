https://www.cnblogs.com/guobin-/p/12572924.html

**一、Activity之间相互跳转：**



```
Intent intent=new Intent(MainActivity.this, InfoActivity.class);
startActivity(intent);
```

　　这种是常规操作，无需多做解释。

　　使用 Activity的startActivity方法，不会有任何限制，因为Activity**继承**自Context，重载了startActivity方法。

**二、非Activity跳转到Activity中：**

　　这种跳转则需要注意，比如在recyclerview控件的每个view的点击事件中，因为是自定义的Adapter，则需要定义一个运行上下文来启动页面跳转：

　　**1、定义全局变量**



```
private Context mContext;
```

　　**2、使用该全局变量进行页面跳转**



```
Intent intent= new Intent();
intent.setClass(mContext, InfoActivity.class);
intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
mContext.startActivity(intent);
```

　　因为context的startActivity方法，需要开启一个新的task，所以要给intent添加flag，值为**Intent.FLAG_ACTIVITY_NEW_TASK**。

　　

　　**注：**在使用全局变量context时，要**在构造函数里进行初始化**，否则会报错。

　　　　在Activity中将**MainActivity.this**作为参数传入，在Adapter中以**Activity类型**接受该参数并**赋值给context**，完成该全局变量的**初始化**。