## 这里是部署运行说明

#### (1)后端
- 安装 `python3.x`
- 安装 `flask, mysql-connector-python`等插件
- 进入 `./PyCommunity/pythonProject/`
- 运行 `Flask.py`

#### (2)前端
- 安装 `Node.js` 并添加环境变量
- 在终端中输入 `npm install vue -g` 安装 `vue`
- 进入 `./Front`，并输入命令 `npm run dev`

#### (3)数据库
- 安装 `mysql` 并连接数据库
- 输入如下命令创建数据库：
```
CREATE DATABASE BUAA_BBS

use BUAA_BBS

CREATE TABLE USERINFO (User_Id INT NOT NULL,
                      User_Name VARCHAR(30) NOT NULL,
                      User_Password VARCHAR(30) NOT NULL,
                      PRIMARY KEY (User_Name))

CREATE TABLE CONTENT (User_id INT NOT NULL,
                      Title VARCHAR(255),
                      Text VARCHAR(255),
                      Time DATETIME,
                      Position INT NOT NULL,
                      Post_Id INT NOT NULL)

```
- 此时访问 `http://localhost:5173/` 即可