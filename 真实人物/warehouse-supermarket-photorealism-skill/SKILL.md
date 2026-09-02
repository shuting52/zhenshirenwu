---
name: warehouse-supermarket-photorealism
description: >
  用于创建和优化超写实真人摄影图像生成提示词，重点处理明确成年主体、
  中国大型会员制仓储超市、酒水商品展示、自然蹲姿、手机生活抓拍、
  真实皮肤与人体结构、复杂服装材质和负面词控制。
  当用户要求生成仓储超市环境人像、购物抓拍、商品展示或高真实性手机摄影时使用。
---

# Warehouse Supermarket Photorealism Skill

## 目标

将复杂图像需求转换为结构清晰、可执行的正向 Prompt 与 Negative Prompt，优先保证：

1. 主体明确为成年人；
2. 人体、双手、双腿、鞋子与商品关系真实；
3. 中国大型会员制仓储超市场景可信；
4. 手机随手抓拍感强，而非广告或影棚；
5. 皮肤、头发、针织、蕾丝和玻璃材质真实；
6. 避免可识别品牌 Logo、乱码和水印。

## 适用场景

- 超写实真人摄影
- 中国大型仓储会员超市
- 酒水、饮品或商品区域
- 成年女性购物抓拍
- 蹲姿、取货、展示商品
- 28–35mm 等效手机主摄环境人像
- 需要严格控制人体结构和负面词的图像生成

## 不适用场景

- 未成年人主体
- 纯动漫、3D、插画
- 要求复制真实品牌 Logo
- 与图像生成无关的普通任务

## 输入要求

提取：年龄与成年状态、外貌、皮肤、头发、服装、配饰、姿态、手部、商品、
场景、构图、焦段、机位、光线、摄影质感、禁止项和输出语言。

信息不足时，优先使用“真实、自然、非商业棚拍”的默认方案。

## 执行工作流

### Step 1：主体检查
明确使用“成年女性 / adult woman / young adult”，避免幼态化表达。

### Step 2：结构化拆解
按以下顺序整理：

1. Overall Style
2. Subject
3. Face and Skin
4. Hair
5. Outfit
6. Pose and Anatomy
7. Product Interaction
8. Environment
9. Composition and Lens
10. Lighting
11. Photography Texture
12. Negative Constraints

### Step 3：优先级
优先保证：
成年状态 → 人体结构 → 手脚与商品 → 场景真实性 → 构图 → 服装 → 外貌 → 光线 → 文字细节。

### Step 4：姿态控制
复杂蹲姿必须明确：

- 一条腿为主要支撑；
- 另一条腿自然向前折叠；
- 双脚真实着地；
- 膝盖和脚踝方向合理；
- 上半身仅轻微倾斜。

### Step 5：商品控制
明确物理关系：

- right hand grips the bottle neck
- left palm supports the bottle base
- single large amber glass bottle
- no floating object
- no recognizable brand logo

### Step 6：场景控制
仓储超市至少包含多个环境锚点：

- tall industrial metal shelves
- red structural beams
- pallets
- dense beverage packaging
- electronic price tags
- wide gray polished concrete floor
- EXIT / 出口辅助标识

### Step 7：摄影控制
使用：

- friend casually photographed this with a smartphone
- ordinary real-life shopping moment
- 28–35mm equivalent smartphone main camera
- light smartphone HDR
- natural digital sharpening
- background remains recognizable
- not a commercial advertisement
- not a studio photoshoot

### Step 8：负面词分类
按人物、画风、人体、手脚、服装、商品、场景、镜头、文字与水印分类。

## 输出格式

### 1. 场景摘要
3–6 条核心视觉目标。

### 2. 中文完整版 Prompt
按照：整体风格 → 人物 → 外貌 → 服装 → 姿态 → 商品 → 场景 → 构图 → 光线 → 摄影质感。

### 3. English Prompt
保留摄影、材质、镜头与人体控制关键词。

### 4. Negative Prompt
单独输出。

### 5. 参数建议
- Aspect ratio: 3:4
- Camera: 28–35mm equivalent smartphone main camera
- Depth of field: moderate / environment recognizable
- Stylization: low to medium
- Detail: high

## 质量检查

- [ ] 主体明确成年人
- [ ] 双手与商品接触正确
- [ ] 双腿、双脚数量正确
- [ ] 鞋子与脚自然连接
- [ ] 商品不漂浮、不穿模
- [ ] 无真实品牌 Logo
- [ ] 无大面积乱码
- [ ] 场景明显属于大型仓储会员超市
- [ ] 背景可辨识
- [ ] 没有影棚广告感
- [ ] 皮肤、头发、蕾丝、针织和玻璃具有真实纹理

## 异常处理

### 人体错误
减少重复肢体描述，优先保留支撑腿、折叠腿、双脚着地和双手位置。

### 商品漂浮
明确 grip / support 两个动作，并限制为 single large bottle。

### 文字乱码
价格与标签仅作为背景辅助元素，不要求完整复杂文字。

### 广告感过强
增加：
“friend casually photographed this”
“ordinary real-life shopping moment”
“not a commercial advertisement”
“not a studio photoshoot”

## 使用示例

用户：
“生成一名成年东亚女性在中国大型会员制仓储超市酒水区蹲下展示琥珀色瓶装饮品的手机抓拍。”

输出：
1. 场景摘要；
2. 中文完整版 Prompt；
3. English Prompt；
4. Negative Prompt；
5. 参数建议。
