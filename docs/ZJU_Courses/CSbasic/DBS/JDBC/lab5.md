# JDBC 使用案例 - Lab5 图书管理系统

## java基础语法

```java
try {
} catch (Exception e) {
    System.out.println("storeBook: Insert fail.");
    rollback(conn);
    return new ApiResult(false, e.getMessage());
}
        List<Book> query_books = new ArrayList<>();
```

## sql语句使用

```java
Connection conn = connector.getConn();
String query_sql = "SELECT book_id FROM book WHERE category = ?;
PreparedStatement pstmt = conn.prepareStatement(query_sql);
pstmt.setString(1, book.getCategory());
pstmt.setString(2, book.getTitle());
ResultSet res = pstmt.executeQuery();
if(rs.next()) 
pstmt.close();
commit(conn);
```

