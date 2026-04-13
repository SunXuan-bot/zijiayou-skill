# 自驾路线规划Skill

> 基于路线库(827条) + 高德地图API，为用户规划自驾行程（含一键导航链接）

---

## 👤 关于作者

**孙轩（武汉驾到）**

- 旅行爱好者，AI工具实践者
- GitHub: [@SunXuan-bot](https://github.com/SunXuan-bot)
- 微信：`dave0916`（欢迎交流AI + 自驾游）

---

## 💬 交流与合作

这是一个**免费开源的练手项目**，初衷是：
1. **探索AI在自驾游场景中的应用**，用AI提升路线规划效率
2. **与同行交流**，探索AI时代自驾游/旅行行业的可能性

如果你也在做类似的事情，或者对AI+旅行这个方向感兴趣，欢迎加我微信交流。

---


---

## 功能

- ✅ 先问需求（人数/人群/目的地/天数），不盲目给方案
- ✅ 搜路线库（827条全国路线）
- ✅ 调用高德API计算精确里程、高速、过路费、油费
- ✅ 搜索景点POI + 每个景点生成高德导航链接
- ✅ 输出标准路书，可直接发给客户

---

## 数据

- **路线库**：827条全国自驾路线（云南/新疆/西藏/四川/贵州等）
- **地图工具**：高德地图MCP Server（amap）

---

## 快速测试

```bash
# 搜索路线库
python3 scripts/search_routes.py [省份] [天数] [关键词]

# 示例
python3 scripts/search_routes.py 云南 5
python3 scripts/search_routes.py 新疆 10

# 调用高德地图
mcporter call amap.maps_direction_driving_by_address origin_address="武汉" destination_address="昆明"
mcporter call amap.maps_text_search keywords="昆明景点" city="昆明"
```

---

## Skill流程

```
用户触发 → 需求确认三问
    ↓
用户回答 → 搜路线库 + 高德API
    ↓
生成路书 → 每个景点带导航链接
```

---

## 输出示例（每个景点含导航链接）

```
📍【石林风景区】[导航去这里](https://uri.amap.com/navigation?to=103.325701,24.812964,石林风景区&mode=car&src=武汉驾到)
```

---

## 目录结构

```
zijia-luyou-guihua/
├── SKILL.md              # Skill定义（主文件，301行）
├── README.md              # 本文件
├── data/
│   └── routes_travel.json # 路线库（827条）
└── scripts/
    └── search_routes.py   # 路线库搜索脚本
```

---

## 更新日志

- 2026-04-12：v0.2 增强版
  - 新增：需求确认三问流程
  - 新增：每个景点高德导航链接
  - 新增：自驾成本明细（高速费+油费）
  - 新增：途经高速名称
- 2026-04-12：v0.1 初始版本，路线库827条 + 高德API接入
