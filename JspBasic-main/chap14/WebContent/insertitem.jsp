<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page import = "java.sql.DriverManager" %>
<%@ page import = "java.sql.Connection" %>
<%@ page import = "java.sql.PreparedStatement" %>
<%@ page import = "java.sql.SQLException" %>
<%
	String idValue = request.getParameter("id");

	Connection conn = null;
	PreparedStatement pstmtItem = null;
	PreparedStatement pstmtDetail = null;
	
	
	String jdbcDriver = "jdbc:oracle:thin:@localhost:1521:xe";
	String dbUser = "jspexam";
	String dbPass = "1234";
	
	Class.forName("oracle.jdbc.driver.OracleDriver");
	
	Throwable occuredException = null;
	
	try {
		int id = Integer.parseInt(idValue);
		
		conn = DriverManager.getConnection(jdbcDriver, dbUser, dbPass);
		conn.setAutoCommit(false);
		
		pstmtItem = conn.prepareStatement("insert into ITEM value(?, ?)");
		pstmtItem.setInt(1, id);
		pstmtItem.setString(2, "상품 이름" + id);
		pstmtItem.executeUpdate();
		
		if(request.getParameter("error") != null) {
			throw new Exception("의도적 익셉션 발생");
		}
		
		pstmtDetail = conn.prepareStatement(
				"insert into ITEM_DETAIL value(?, ?)");
		pstmtDetail.setInt(1, id);
		pstmtDetail.setString(2, "상세 설명" + id);
		pstmtDetail.executeUpdate();
		
		conn.commit();
	} catch(Throwable e) {
		if (conn != null) {
			try {
				conn.rollback();
			} catch(SQLException ex) {}
		}
		occuredException = e;
	} finally {
		if(pstmtItem != null)
			try { pstmtItem.close(); } catch(SQLException ex) {}
		if(pstmtDetail != null)
			try { pstmtDetail.close(); } catch(SQLException ex) {}
		if(conn != null) try { conn.close(); } catch(SQLException ex) {}
	}
%>
<html>
<head><title> ITEM 값 입력</title></head>
<body>

<% if(occuredException != null) { %>
에러가 발생하였슴: <%= occuredException.getMessage() %>
<% } else { %>
데이터가 성공적으로 들어감
<% } %>
</body>
</html>