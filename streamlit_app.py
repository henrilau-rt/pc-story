#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
 🏫 《紅藍時空尋根記》 - 香港培正小學尋根之旅 2D RPG (Streamlit Web App)
=============================================================================
 支援本機 Streamlit 運行及直接部署至 Streamlit Community Cloud (免費雲端網址)
 
 本機執行方式：
   pip install streamlit
   streamlit run streamlit_app.py
=============================================================================
"""

import os
import streamlit as st
import streamlit.components.v1 as components

import streamlit as st
import streamlit.components.v1 as components

# 強制隱藏右下角 Profile Badge 與彈出視窗
components.html(
    """
    <script>
    function hideBadge() {
        // 同時搜尋當前視窗與父層視窗
        const docs = [document];
        try {
            if (window.parent && window.parent.document) {
                docs.push(window.parent.document);
            }
        } catch (e) {}

        docs.forEach(doc => {
            // 隱藏右下角個人資料卡片、頭像按鈕與浮動元素
            const selectors = [
                'div[class*="ProfileBadge"]',
                'div[class*="profileBadge"]',
                'div[class*="viewerBadge"]',
                'div[class*="manageApp"]',
                'div[data-testid="stStatusWidget"]',
                'a[href*="share.streamlit.io/user"]',
                'button[aria-label*="profile"]'
            ];
            
            selectors.forEach(selector => {
                const elements = doc.querySelectorAll(selector);
                elements.forEach(el => {
                    el.style.display = 'none';
                    el.style.visibility = 'hidden';
                    el.style.opacity = '0';
                    el.style.pointerEvents = 'none';
                });
            });
        });
    }

    // 定期檢查以防 Streamlit 動態載入後重新出現
    hideBadge();
    const interval = setInterval(hideBadge, 500);
    setTimeout(() => clearInterval(interval), 10000);
    </script>
    """,
    height=0,
    width=0,
)

# test code


# 頁面配置
st.set_page_config(
    page_title="紅藍時空尋根記 - 香港培正小學尋根之旅 RPG",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自訂 Streamlit CSS
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
        max-width: 1050px;
    }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .game-header {
        background: linear-gradient(90deg, #d32f2f 0%, #1565c0 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 10px;
        margin-bottom: 14px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .game-header h2 {
        margin: 0;
        font-size: 1.35rem;
        color: white;
    }
    .game-header span {
        font-size: 0.9rem;
        color: #fef08a;
    }
</style>
""", unsafe_allow_html=True)

# 讀取遊戲 HTML 代碼
HTML_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

game_html = ""
if os.path.exists(HTML_FILE_PATH):
    with open(HTML_FILE_PATH, "r", encoding="utf-8") as f:
        game_html = f.read()
else:
    # 嘗試從同目錄上級讀取
    alt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "game", "index.html")
    if os.path.exists(alt_path):
        with open(alt_path, "r", encoding="utf-8") as f:
            game_html = f.read()

# 側邊欄：遊戲指南與歷史背景
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/zh/thumb/d/d4/Pui_Ching_Middle_School_Logo.svg/200px-Pui_Ching_Middle_School_Logo.svg.png", width=90)
    st.title("🎒 尋根之旅小助手")
    st.markdown("""
    **香港培正小學 小五尋根之旅**
    * **校訓**：至善至正
    * **校色**：紅（熱情/愛心）與 藍（冷靜/機智）
    * **創校**：1889 年 11 月 28 日（廣州創校）
    
    ---
    ### 🎮 操作指引
    * **移動**：鍵盤方向鍵 或 `W` `A` `S` `D`
    * **觸控**：支援 iPad / 手機虛擬方向鍵
    * **互動 / 答題**：按 `[E]` 鍵、空白鍵或點擊「互動」按鈕
    * **音樂**：點擊遊戲右上方「🔊 音樂」開關
    
    ---
    ### 🌟 登場傑出校友
    * **崔琦 教授 (輝社)**：諾貝爾物理學獎得主
    * **丘成桐 教授 (協社)**：菲爾茲數學獎得主
    * **鍾景輝 博士 (仁社)**：戲劇大師兼資深校友
    """)

# 主視窗頂部欄
st.markdown("""
<div class="game-header">
    <div>
        <h2>🏫 紅藍時空尋根記</h2>
        <span>香港培正小學 · 小五尋根之旅 2D RPG 探索遊戲</span>
    </div>
    <div style="text-align:right;">
        <span style="background:rgba(255,255,255,0.2); padding:4px 10px; border-radius:15px; font-weight:bold;">
            至善至正 · 永為真理之干城
        </span>
    </div>
</div>
""", unsafe_allow_html=True)

# 渲染 2D RPG 遊戲元件
if game_html:
    components.html(game_html, height=720, scrolling=False)
else:
    st.error("未能找到遊戲 index.html 檔案，請確保 index.html 與 streamlit_app.py 放在同一資料夾內！")

# 頁尾說明
st.caption("💡 提示：在平板或電腦上遊玩時，可按鍵盤 F11 進入全螢幕體驗更佳效果！")
