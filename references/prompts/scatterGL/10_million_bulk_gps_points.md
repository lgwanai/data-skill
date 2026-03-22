## 图表类型：1 千万 GPS 点可视化 (10 million Bulk GPS points)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
var dataCount = 0;
var CHUNK_COUNT = 230;
// https://blog.openstreetmap.org/2012/04/01/bulk-gps-point-data/
function fetchData(idx) {
  if (idx >= CHUNK_COUNT) {
    return;
  }
  var dataURL = ROOT_PATH + '/data/asset/data/gps/gps_' + idx + '.bin';
  var xhr = new XMLHttpRequest();
  xhr.open('GET', dataURL, true);
  xhr.responseType = 'arraybuffer';
  xhr.onload = function (e) {
    var rawData = new Int32Array(this.response);
    var data = new Float32Array(rawData.length);
    var addedDataCount = rawData.length / 2;
    for (var i = 0; i < rawData.length; i += 2) {
      data[i] = rawData[i + 1] / 1e7;
      data[i + 1] = rawData[i] / 1e7;
    }
    myChart.appendData({
      seriesIndex: 0,
      data: data
    });
    fetchData(idx + 1);
  };
  xhr.send();
}
option = {
  backgroundColor: '#000',
  title: {
    text: '10000000 GPS Points',
    left: 'center',
    textStyle: {
      color: '#fff'
    }
  },
  geo: {
    map: 'world',
    roam: true,
    label: {
      emphasis: {
        show: false
      }
    },
    silent: true,
    itemStyle: {
      normal: {
        areaColor: '#323c48',
        borderColor: '#111'
      },
      emphasis: {
        areaColor: '#2a333d'
      }
    }
  },
  series: [
    {
      name: '弱',
      type: 'scatterGL',
      progressive: 1e6,
      coordinateSystem: 'geo',
      symbolSize: 1,
      zoomScale: 0.002,
      blendMode: 'lighter',
      large: true,
      itemStyle: {
        color: 'rgb(20, 15, 2)'
      },
      postEffect: {
        enable: true
      },
      silent: true,
      dimensions: ['lng', 'lat'],
      data: new Float32Array()
    }
  ]
};
fetchData(0);
```

