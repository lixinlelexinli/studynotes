手动添加kernel

1. 切换到需要配置的环境

```
activate 环境名
```

2. 安装ipykernel

   ```python
   pip install ipykernel
   ```

3. 手动添加这个kernel

   ```python
   python -m ipykernel install --name 环境名 --display-name "notebook中显示的kernel名"
   ```

4. 查看当前所有可用的kernel

   ```
   jupyter kernelspec list
   ```

   