# Stacked Pull Request 가이드

## 개요

Stacked Pull Request는 여러 개의 연관된 변경사항을 독립적으로 리뷰할 수 있도록 작은 단위로 나누어 PR을 만드는 전략입니다. 각 PR은 이전 PR을 기반으로 하여 순차적으로 리뷰하고 병합할 수 있습니다.

## Git Flow 기반 Stacked PR 구조

이 레포지토리에서는 다음과 같은 구조를 사용합니다:

```
develop
  └── feature-a-1 (PR #1)
        └── feature-a-2 (PR #2)
              └── feature-a-3 (PR #3)
```

각 브랜치는 이전 브랜치를 기반으로 생성되며, 순차적으로 병합됩니다.

## 기본 워크플로우

### 1. 첫 번째 피쳐 브랜치 생성

```bash
# develop 브랜치에서 시작
git checkout develop
git pull origin develop

# 첫 번째 피쳐 브랜치 생성
git checkout -b feature-a-1
# 코드 작성 및 커밋
git add .
git commit -m "feat: feature-a-1 구현"
git push -u origin feature-a-1
```

### 2. 두 번째 피쳐 브랜치 생성

```bash
# feature-a-1을 기반으로 생성
git checkout feature-a-1
git checkout -b feature-a-2
# 코드 작성 및 커밋
git add .
git commit -m "feat: feature-a-2 구현"
git push -u origin feature-a-2
```

### 3. 세 번째 피쳐 브랜치 생성

```bash
# feature-a-2를 기반으로 생성
git checkout feature-a-2
git checkout -b feature-a-3
# 코드 작성 및 커밋
git add .
git commit -m "feat: feature-a-3 구현"
git push -u origin feature-a-3
```

## 리뷰 반영 후 브랜치 갱신하기

**가장 중요한 부분**: `feature-a-1`에 리뷰가 반영되어 코드가 수정되었을 때, `feature-a-2`와 `feature-a-3`를 효율적으로 갱신하는 방법입니다.

### 시나리오

1. `feature-a-1` PR에 리뷰가 달림
2. 리뷰를 반영하여 `feature-a-1` 브랜치에 새로운 커밋 추가
3. 이제 `feature-a-2`와 `feature-a-3`도 최신 `feature-a-1`을 반영해야 함

### 효율적인 갱신 방법

#### 방법 1: Rebase를 사용한 순차적 갱신 (권장)

이 방법은 각 브랜치를 순차적으로 rebase하여 깔끔한 히스토리를 유지합니다.

```bash
# 1. feature-a-1의 최신 변경사항을 가져옴
git checkout feature-a-1
git pull origin feature-a-1

# 2. feature-a-2를 feature-a-1 위로 rebase
git checkout feature-a-2
git rebase feature-a-1

# 충돌이 발생하면 해결 후
git add .
git rebase --continue

# 3. force push (주의: 이미 PR이 열려있는 경우에만)
git push --force-with-lease origin feature-a-2

# 4. feature-a-3를 feature-a-2 위로 rebase
git checkout feature-a-3
git rebase feature-a-2

# 충돌이 발생하면 해결 후
git add .
git rebase --continue

# 5. force push
git push --force-with-lease origin feature-a-3
```

#### 방법 2: Merge를 사용한 갱신

Rebase보다 안전하지만 히스토리가 복잡해질 수 있습니다.

```bash
# 1. feature-a-1의 최신 변경사항을 가져옴
git checkout feature-a-1
git pull origin feature-a-1

# 2. feature-a-2에 feature-a-1 병합
git checkout feature-a-2
git merge feature-a-1

# 충돌이 발생하면 해결 후
git add .
git commit -m "chore: feature-a-1의 최신 변경사항 반영"
git push origin feature-a-2

# 3. feature-a-3에 feature-a-2 병합
git checkout feature-a-3
git merge feature-a-2

# 충돌이 발생하면 해결 후
git add .
git commit -m "chore: feature-a-2의 최신 변경사항 반영"
git push origin feature-a-3
```

### 왜 Rebase가 더 효율적인가?

1. **깔끔한 히스토리**: 각 피쳐의 변경사항이 선형적으로 유지됩니다
2. **명확한 의존성**: 각 브랜치가 정확히 이전 브랜치를 기반으로 함을 보장합니다
3. **리뷰 용이성**: PR diff가 더 명확하고 이해하기 쉽습니다

### 주의사항

⚠️ **Force Push 주의사항**:
- `--force-with-lease`를 사용하여 실수로 다른 사람의 작업을 덮어쓰지 않도록 합니다
- 이미 PR이 열려있는 경우에만 force push를 사용합니다
- 팀원들과 협의 후 사용하세요

## 실제 예제

이 레포지토리에는 실제 예제가 포함되어 있습니다:

- `feature-a-1`: 첫 번째 피쳐 브랜치 (PR #1)
- `feature-a-2`: 두 번째 피쳐 브랜치 (PR #2)
- `feature-a-3`: 세 번째 피쳐 브랜치 (PR #3)

각 브랜치의 PR을 확인하고, `feature-a-1`에 리뷰를 반영한 후 위의 방법으로 갱신해보세요.

## 병합 순서

Stacked PR은 항상 **아래에서 위로** 순차적으로 병합해야 합니다:

1. `feature-a-1` → `develop` (먼저 병합)
2. `feature-a-2` → `develop` (그 다음 병합)
3. `feature-a-3` → `develop` (마지막 병합)

이 순서를 지키지 않으면 충돌이 발생할 수 있습니다.

## 자주 묻는 질문 (FAQ)

### Q: feature-a-1이 병합된 후에는 어떻게 하나요?

A: `feature-a-2`와 `feature-a-3`의 base 브랜치를 `develop`으로 변경하거나, `develop`을 rebase하여 갱신할 수 있습니다.

```bash
# feature-a-1이 develop에 병합된 후
git checkout feature-a-2
git rebase develop
git push --force-with-lease origin feature-a-2
```

### Q: 여러 사람이 동시에 작업할 때는?

A: 각 피쳐 브랜치를 다른 개발자가 담당하거나, 순차적으로 작업하는 것이 좋습니다. 동시 작업 시 충돌 가능성이 높아집니다.

### Q: feature-a-2만 수정이 필요하면?

A: `feature-a-2`만 수정하고, `feature-a-3`를 `feature-a-2` 위로 rebase하면 됩니다.

## 참고 자료

- [Git Rebase 공식 문서](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)
- [Stacked Diffs 가이드](https://graphite.dev/blog/stacked-diffs)

