package mvc.simple;

import java.io.IOException;
import java.io.javax.servlet.RequestDispatcher;
import java.io.javax.servlet.ServletException;
import java.io.javax.servlet.http.HttpServlet;
import java.io.javax.servlet.http.HttpServletRequest;
import java.io.javax.servlet.http.HttpServletResponse;

public class SimpleController extends HttpServlet {
	
	public void doGet(HttpServletRequest request, HttpServletResponse response)
	throws ServletException, IOException {
		processRequest(request, response);
	}
	
	public void doPost(HttpServletRequest request,
			HttpServletResponse response)
	throws ServletException, IOException {
		processRequest(request, response);
	}
	
	private void processRequest(javax.servlet.http.HttpServletRequest request,
			HttpServletResponse response)
	throws IOException, ServletException {
		// 2단계 요청파악
		// request 객체로 부터 사용자의 요청을 파악하는 코드
		String type = request.getParameter("type");
		
		// 3단계 요청한 기능을 수행한다.
		// 사용자에 요청에 따라 알맞은 코드.
		Object resultObject = null;
		if (type == null || type.equals("greeting")) {
			resultObject = "안녕하세요.";
		} else if (type.equals("date")) {
			resultObject = new java.util.Date();
		} else {
			resultObject = "Invalid Type";
		} 
		
		// 4단계, request나 session에 처리결과를 저장
		request.setAttribute("result", resultObject);
		
		// 5단계, RequestDispatcher를 사용하여 알맞는 뷰로 포워딩
		RequestDispatcher dispatcher =
				request.getRequestDispatcher("/simpleView.jsp");
		dispatcher.forward(request, response);
	}
}
