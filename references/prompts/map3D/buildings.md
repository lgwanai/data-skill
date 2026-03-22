## 图表类型：三维建筑 (Buildings)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### 外部数据结构分析
该图表需要特定的外部数据结构支撑。以下是下载后的数据结构示例，请将用户的真实数据映射为类似结构：

**数据文件 [/data-gl/asset/data/buildings.json]**:
```json
数据是一个对象 (Object)。包含的顶层字段示例：features, UTF8Encoding, UTF8Scale。数据截取示例：
{
  "features": [
    {
      "type": "Feature",
      "properties": {
        "name": "0",
        "height": 0.7
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          "@@Ӽѻ࡮ϐ˥ɾ؝ʳmpȓǮʣĻ"
        ],
        "encodeOffsets": [
          [
            13368440,
            52534490
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "name": "1",
        "height": 0
      },
      "geometry": {
        "type": "Polygo...
```

### 图片资源提示
该图表需要加载以下类型的图片资源：
https://echarts.apache.org/examples/data-gl/asset/pisa.hdr
请在生成代码时保留图片 URL 参数位置，并在最终输出时明确提示用户提供相应的图片资源 URL。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
$.getJSON(
  ROOT_PATH + '/data-gl/asset/data/buildings.json',
  function (buildingsGeoJSON) {
    echarts.registerMap('buildings', buildingsGeoJSON);
    var regions = buildingsGeoJSON.features.map(function (feature) {
      return {
        name: feature.properties.name,
        value: Math.random(),
        height: feature.properties.height / 10
      };
    });
    myChart.setOption({
      visualMap: {
        show: false,
        min: 0.4,
        max: 1,
        inRange: {
          color: [ /* 请使用用户的真实数据数组替换此处 */ ]
        }
      },
      series: [
        {
          type: 'map3D',
          map: 'buildings',
          shading: 'realistic',
          environment: '#000',
          realisticMaterial: {
            roughness: 0.6,
            textureTiling: 20
          },
          postEffect: {
            enable: true,
            SSAO: {
              enable: true,
              intensity: 1.3,
              radius: 5
            },
            screenSpaceReflection: {
              enable: false
            },
            depthOfField: {
              enable: true,
              blurRadius: 4,
              focalDistance: 30
            }
          },
          light: {
            main: {
              intensity: 3,
              alpha: 40,
              shadow: true,
              shadowQuality: 'high'
            },
            ambient: {
              intensity: 0
            },
            ambientCubemap: {
              texture: ROOT_PATH + '/data-gl/asset/pisa.hdr',
              exposure: 1,
              diffuseIntensity: 0.5,
              specularIntensity: 1
            }
          },
          groundPlane: {
            show: false,
            color: '#333'
          },
          viewControl: {
            minBeta: -360,
            maxBeta: 360,
            alpha: 50,
            center: [50, 0, -10],
            distance: 30,
            minDistance: 5,
            panMouseButton: 'left',
            rotateMouseButton: 'middle',
            zoomSensitivity: 0.5
          },
          itemStyle: {
            areaColor: '#666'
            // borderColor: '#222',
            // borderWidth: 1
          },
          label: {
            color: 'white'
          },
          silent: true,
          instancing: true,
          boxWidth: 200,
          boxHeight: 1,
          data: regions
        }
      ]
    });
  }
);
```

