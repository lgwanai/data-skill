## 图表类型： (Airline on Globe)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data-gl/asset/data/flights.json]**:
```json
数据是一个对象 (Object)。包含的顶层字段示例：airportsFields, airlineFields, airports, airlines, routes。数据截取示例：
{
  "airportsFields": [
    "name",
    "city",
    "country",
    "longitude",
    "latitude"
  ],
  "airlineFields": [
    "name",
    "country"
  ],
  "airports": [
    [
      "Goroka",
      "Goroka",
      "Papua New Guinea",
      145.391881,
      -6.081689
    ],
    [
      "Madang",
      "Madang",
      "Papua New Guinea",
      145.7887,
      -5.207083
    ],
    [
      "Mount Hagen",
      "Mount Hagen",
      "Papua New Guinea",
      144.295861,
      -5.826789
    ],
    [
   ...
```

### 图片资源提示
该图表需要加载以下类型的图片资源：
https://echarts.apache.org/examples/data-gl/asset/world.topo.bathy.200401.jpg
https://echarts.apache.org/examples/data-gl/asset/bathymetry_bw_composite_4k.jpg
请在生成代码时保留图片 URL 参数位置，并在最终输出时明确提示用户提供相应的图片资源 URL。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.getJSON(ROOT_PATH + '/data-gl/asset/data/flights.json', function (data) {
  function getAirportCoord(idx) {
    return [data.airports[idx][3], data.airports[idx][4]];
  }
  var routes = data.routes.map(function (airline) {
    return [getAirportCoord(airline[1]), getAirportCoord(airline[2])];
  });
  myChart.setOption({
    backgroundColor: '#000',
    globe: {
      baseTexture: ROOT_PATH + '/data-gl/asset/world.topo.bathy.200401.jpg',
      heightTexture:
        ROOT_PATH + '/data-gl/asset/bathymetry_bw_composite_4k.jpg',
      shading: 'lambert',
      light: {
        ambient: {
          intensity: 0.4
        },
        main: {
          intensity: 0.4
        }
      },
      viewControl: {
        autoRotate: false
      }
    },
    series: {
      type: 'lines3D',
      coordinateSystem: 'globe',
      blendMode: 'lighter',
      lineStyle: {
        width: 1,
        color: 'rgb(50, 50, 150)',
        opacity: 0.1
      },
      data: routes
    }
  });
});
```

