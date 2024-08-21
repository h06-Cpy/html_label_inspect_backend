# HTML 테이블 라벨링 검수-백엔드

- 서버 내 json 레이블 수정
- 생성된 테이블 이미지를 서버에 저장
- 데이터베이스에 html, 이미지 경로 저장

## Tech Stack
- Python
- FastAPI
- SQLite3

## API Spec
### `POST` /save_label
html 및 생성된 이미지 저장

request
```json
{
	"originId": int
	"html": string,
	"savedImage": string(base64)
}
```

response
```json
{
	"success": boolean,
	"message": string
}
```

### `GET` /label_info/{origin_id}
`origin_id`: int

레이블 정보 가져오기
- 검수 여부
- 원본 html
- 총 생성된 이미지 개수

response
```json
{
	"isInspected": boolean,
	"originHtml": string,
	"totalGeneratedNum": int
}
```

## Database Scheme
```sql
CREATE TABLE label_info(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        origin_id INTEGER,
                        origin_image_path TEXT,
                        save_image_path TEXT, 
                        html TEXT
                        )
```