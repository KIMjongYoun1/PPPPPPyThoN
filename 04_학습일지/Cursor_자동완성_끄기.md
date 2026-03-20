# Cursor에서 자동완성·AI 제안 끄기

`.vscode/settings.json`만으로도 줄이지만, **Cursor 자체 기능**은 앱 설정에서 따로 꺼야 할 수 있습니다.

## 1. Cursor 설정 (앱)

1. **Cmd + ,** (Mac) 또는 **Ctrl + ,** (Windows) → 설정 열기  
2. 검색창에 아래 키워드로 찾아 **끄기**:

| 검색어 | 끌 것 |
|--------|--------|
| `Cursor Tab` | **Disable** (인라인 회색 제안, Tab으로 받기) |
| `inline` | 인라인 제안 관련 항목 |
| `Copilot` | GitHub Copilot 쓰는 경우 |

3. **Cursor → Settings → Cursor Settings** (또는 Features)에서  
   **Autocomplete / Tab completion** 를 끄는 옵션이 있으면 OFF

## 2. 이 프로젝트 (이미 적용됨)

`Python/.vscode/settings.json`:

- `editor.suggest.enabled`: false — 제안 위젯 전체
- `editor.inlineSuggest.enabled`: false — 인라인 제안 (Copilot 스타일)
- `github.copilot.enable`: false — Copilot 확장 사용 시

## 3. 적용이 안 될 때

- **창 다시 로드**: `Cmd+Shift+P` → `Developer: Reload Window`
- **사용자 설정이 이기는 경우**:  
  사용자 `settings.json`에 `editor.suggest.enabled: true` 등이 있으면 제거하거나 false로 맞추기

## 4. 다시 켜고 싶을 때

- `.vscode/settings.json`에서 위 항목 삭제 또는 true로 변경  
- Cursor에서 Cursor Tab 다시 Enable
