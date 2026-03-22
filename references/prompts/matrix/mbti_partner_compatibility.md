## 图表类型：MBTI 伴侣相容性 (MBTI Partner Compatibility)

**生成指令**：你现在的任务是生成一个 ECharts 的 `option` 配置。请根据以下骨架代码和数据结构要求，结合用户的实际数据进行填充和修改，生成一份完整的图表配置参数。

### ECharts Option 骨架参考
请基于此结构（已剥离冗长写死的数据）生成配置。不要直接输出此骨架，而是要输出**包含真实数据和完整逻辑**的完整 `option` 对象：

```javascript
// Click on the data to toggle grouping
const mbti = [ /* 请使用用户的真实数据数组替换此处 */ ];
const color = {
  green: '#2D9A69',
  purple: '#7D568F',
  blue: '#3A8DAB',
  yellow: '#E0A433',
  greenLighter: '#10CA77',
  purpleLighter: '#9253AF',
  blueLighter: '#26A9D9',
  yellowLighter: '#F4AC24',
  greenDarker: '#0FB369',
  purpleDarker: '#854AA0',
  blueDarker: '#2298C3',
  yellowDarker: '#F2A30D'
};
const fontSize = {
  group: window.innerHeight > 700 ? 24 : 16,
  item: window.innerHeight > 700 ? 13 : 11,
  value: window.innerHeight > 700 ? 15 : 12
};
const getColor = (mbti, lightness = 0) => {
  if (mbti.indexOf('NF') >= 0) {
    return lightness < 0
      ? color.greenLighter
      : lightness > 0
      ? color.greenDarker
      : color.green;
  }
  if (mbti.indexOf('NT') >= 0) {
    return lightness < 0
      ? color.purpleLighter
      : lightness > 0
      ? color.purpleDarker
      : color.purple;
  }
  if (mbti.indexOf('S') >= 0 && mbti.indexOf('J') >= 0) {
    return lightness < 0
      ? color.blueLighter
      : lightness > 0
      ? color.blueDarker
      : color.blue;
  }
  if (mbti.indexOf('S') >= 0 && mbti.indexOf('P') >= 0) {
    return lightness < 0
      ? color.yellowLighter
      : lightness > 0
      ? color.yellowDarker
      : color.yellow;
  }
};
const generateGroup = (groupName) => {
  const colorMap = {
    NF: color.green,
    NT: color.purple,
    SJ: color.blue,
    SP: color.yellow
  };
  const groupMembers = {
    NF: ['INFJ', 'INFP', 'ENFJ', 'ENFP'],
    NT: ['INTJ', 'INTP', 'ENTJ', 'ENTP'],
    SJ: ['ISFJ', 'ISTJ', 'ESFJ', 'ESTJ'],
    SP: ['ISFP', 'ISTP', 'ESFP', 'ESTP']
  };
  return {
    value: groupName,
    label: {
      color: colorMap[groupName],
      fontSize: fontSize.group,
      fontWeight: 'bolder',
      padding: 0
    },
    children: groupMembers[groupName].map((mbti) => ({
      value: mbti,
      label: {
        color: colorMap[groupName],
        fontSize: fontSize.item,
        fontWeight: 'bold'
      }
    }))
  };
};
const xData = [
  generateGroup('NF'),
  generateGroup('NT'),
  generateGroup('SJ'),
  generateGroup('SP')
];
const yData = [
  generateGroup('NF'),
  generateGroup('NT'),
  generateGroup('SJ'),
  generateGroup('SP')
];
const originalData = [ /* 请使用用户的真实数据数组替换此处 */ ];
const dataMap = new Map();
const avgData = {};
for (const [a, b, v] of originalData) {
  dataMap.set(`${a}-${b}`, v);
}
const heatmapData = [];
const scatterData = [];
const decalSize = 1;
for (const a of mbti) {
  for (const b of mbti) {
    const key = `${a}-${b}`;
    const altKey = `${b}-${a}`;
    let value;
    if (dataMap.has(key)) {
      value = [a, b, dataMap.get(key)];
    } else if (dataMap.has(altKey)) {
      value = [a, b, dataMap.get(altKey)];
    } else {
      value = [a, b, 0];
    }
    heatmapData.push({
      value,
      itemStyle: {
        decal: {
          shape: 'circle',
          symbolSize: 1,
          color: getColor(a, 1),
          backgroundColor: getColor(b, 1),
          dashArrayX: [
            [decalSize, decalSize],
            [0, decalSize, decalSize, 0]
          ],
          dashArrayY: [decalSize, 0]
        },
        borderColor: getColor(b),
        borderWidth: 0
      }
    });
    scatterData.push({
      value,
      label: {
        color: value[2] < 0.2 ? getColor(b) : '#fff',
        opacity: value[2] < 0.15 ? 0.6 : 1
      }
    });
  }
}
const size = Math.round(Math.min(window.innerWidth, window.innerHeight) * 0.9);
const fontFamily = 'Ubuntu Condensed, sans-serif';
const detailSeries = [
  {
    id: 'detail-heatmap',
    type: 'heatmap',
    coordinateSystem: 'matrix',
    data: heatmapData,
    label: {
      show: false
    },
    emphasis: {
      itemStyle: {
        borderWidth: 5
      }
    }
  },
  {
    id: 'detail-scatter',
    type: 'scatter',
    coordinateSystem: 'matrix',
    symbolSize: 0,
    data: scatterData,
    color: '#fff',
    label: {
      show: true,
      formatter: (params) => Math.round(params.value[2] * 100) + '%',
      fontWeight: 'bold',
      color: 'inherit'
    },
    silent: true
  }
];
const getGroup = (mbti) => {
  if (mbti.indexOf('NF') >= 0) {
    return 'NF';
  }
  if (mbti.indexOf('NT') >= 0) {
    return 'NT';
  }
  if (mbti[1] === 'S' && mbti[3] === 'J') {
    return 'SJ';
  }
  if (mbti[1] === 'S' && mbti[3] === 'P') {
    return 'SP';
  }
  return '';
};
const groupRawData = {};
for (let i = 0; i < originalData.length; ++i) {
  const [a, b, v] = originalData[i];
  const groupA = getGroup(a);
  const groupB = getGroup(b);
  const key = groupA > groupB ? `${groupA}-${groupB}` : `${groupB}-${groupA}`;
  if (groupRawData[key]) {
    groupRawData[key].push(v);
  } else {
    groupRawData[key] = [v];
  }
}
const groupData = [];
function median(arr) {
  const sorted = arr.slice().sort((a, b) => a - b);
  const mid = Math.floor(sorted.length / 2);
  if (sorted.length % 2 === 0) {
    return (sorted[mid - 1] + sorted[mid]) / 2;
  } else {
    return sorted[mid];
  }
}
for (const key in groupRawData) {
  if (groupRawData.hasOwnProperty(key)) {
    const [a, b] = key.split('-');
    const v = median(groupRawData[key]);
    const colorA = getColor(a, 1);
    const colorB = getColor(b, 1);
    const label = {
      color: v < 0.2 ? getColor(b) : '#fff',
      fontSize: fontSize.value,
      fontWeight: 'bold',
      opacity: v < 0.15 ? 0.6 : 1,
      formatter: (params) => {
        return `${Math.round(params.value[2] * 100)}%`;
      }
    };
    const decalSize = 3;
    const itemStyle = {
      decal: {
        shape: 'circle',
        symbolSize: 1,
        color: colorA,
        backgroundColor: colorB,
        dashArrayX: [
          [decalSize, decalSize],
          [0, decalSize, decalSize, 0]
        ],
        dashArrayY: [decalSize, 0]
      },
      borderColor: getColor(b),
      borderWidth: 0
    };
    groupData.push({
      value: [a, b, v],
      label,
      itemStyle
    });
    if (a !== b) {
      groupData.push({
        value: [b, a, v],
        label,
        itemStyle
      }); // Symmetric
    }
  }
}
const groupSeries = [
  {
    id: 'summary-heatmap',
    type: 'heatmap',
    coordinateSystem: 'matrix',
    data: groupData,
    label: {
      show: true
    }
  }
];
option = {
  backgroundColor: '#F0F7F9',
  textStyle: {
    fontFamily
  },
  title: {
    text: 'MBTI Partner Compatibility',
    subtext:
      'Data from: https://www.personalitydata.org/16-types/enfj-relationships#partner-matrix',
    sublink:
      'https://www.personalitydata.org/16-types/enfj-relationships#partner-matrix',
    left: 'center',
    top: 5,
    textStyle: {
      fontSize: 20,
      color: '#57576A'
    },
    itemGap: 5
  },
  tooltip: {
    formatter: (params) => {
      return `<span style="color:${getColor(
        params.value[1]
      )};font-weight:bold">${params.value[1]}</span> /
                            <span style="color:${getColor(
                              params.value[0]
                            )};font-weight:bold">${params.value[0]}</span> :
                            ${Math.round(params.value[2] * 100)}%`;
    },
    borderColor: '#eee',
    padding: [2, 8]
  },
  matrix: {
    x: {
      data: xData,
      itemStyle: {
        borderColor: 'transparent',
        borderWidth: 0
      },
      dividerLineStyle: {
        width: 0
      },
      label: {
        fontFamily
      },
      levels: [
        {
          levelSize: 25
        },
        {
          levelSize: 30
        }
      ]
    },
    y: {
      data: yData,
      itemStyle: {
        borderColor: 'transparent',
        borderWidth: 0
      },
      dividerLineStyle: {
        width: 0
      },
      label: {
        fontFamily
      }
    },
    body: {
      itemStyle: {
        borderWidth: 0
      },
      label: {
        fontFamily
      }
    },
    width: size,
    height: size,
    left: (window.innerWidth - size) / 2,
    top: 50,
    backgroundStyle: {
      color: 'transparent',
      borderColor: 'transparent',
      borderWidth: 0
    }
  },
  visualMap: [
    {
      type: 'continuous',
      min: 0,
      max: 1,
      dimension: 2,
      calculable: true,
      orient: 'horizontal',
      top: 5,
      left: 'center',
      inRange: {
        opacity: [0, 1]
      },
      seriesIndex: [0, 2],
      show: false
    }
  ],
  series: detailSeries,
  aria: {
    enabled: true,
    decal: {
      show: true
    }
  },
  animation: 0
};
let isGroup = false;
myChart.on('click', () => {
  isGroup = !isGroup;
  option.series = isGroup ? groupSeries : detailSeries;
  myChart.setOption(option, true);
});
```

