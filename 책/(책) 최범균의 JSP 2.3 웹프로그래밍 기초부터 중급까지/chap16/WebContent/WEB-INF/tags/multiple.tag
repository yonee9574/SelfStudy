<%@ tag language="java" pageEncoding="UTF-8"%>
<%@ tag trimDirectiveWhitespaces="ture" %>
<%@ attribute name="count" required="ture" type="java.lang.Integer"%>
<%@ taglib prefix = "c" uri="http://java.sun.com/jsp/jst1/core"%>
<c:forEach begin = "${1}" end="${count}">
<jsp:doBody />
</c:forEach>
