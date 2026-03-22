## 图表类型： (Flights GL)

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

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
var uploadedDataURL = ROOT_PATH + '/data-gl/asset/data/flights.json';
myChart.showLoading();
$.getJSON(uploadedDataURL, function (data) {
  myChart.hideLoading();
  function getAirportCoord(idx) {
    return [data.airports[idx][3], data.airports[idx][4]];
  }
  var routes = data.routes.map(function (airline) {
    return [getAirportCoord(airline[1]), getAirportCoord(airline[2])];
  });
  myChart.setOption({
    geo3D: {
      map: 'world',
      shading: 'realistic',
      silent: true,
      environment: '#333',
      realisticMaterial: {
        roughness: 0.8,
        metalness: 0
      },
      postEffect: {
        enable: true
      },
      groundPlane: {
        show: false
      },
      light: {
        main: {
          intensity: 1,
          alpha: 30
        },
        ambient: {
          intensity: 0
        }
      },
      viewControl: {
        distance: 70,
        alpha: 89,
        panMouseButton: 'left',
        rotateMouseButton: 'right'
      },
      itemStyle: {
        color: '#000'
      },
      regionHeight: 0.5
    },
    series: [
      {
        type: 'lines3D',
        coordinateSystem: 'geo3D',
        effect: {
          show: true,
          trailWidth: 1,
          trailOpacity: 0.5,
          trailLength: 0.2,
          constantSpeed: 5
        },
        blendMode: 'lighter',
        lineStyle: {
          width: 0.2,
          opacity: 0.05
        },
        data: routes
      }
    ]
  });
  window.addEventListener('keydown', function () {
    myChart.dispatchAction({
      type: 'lines3DToggleEffect',
      seriesIndex: 0
    });
  });
});
```

