<%@ page contentType="text/html; charset=UTF-8"%>
<%@ page import = "java.util.Date" %>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jst1/core" %>
<jsp:doBody var = "bodyText" />
<c:out value = "${bodyText}" escapeXml="true"/>