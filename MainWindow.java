import javax.swing.JFrame;
import java.awt.Color;
import java.awt.Insets;
import java.awt.color.ColorSpace;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.Dimension;
import java.io.File;
import java.math.BigInteger;
import javax.swing.JPanel;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.HeadlessException;

import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JTextField;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.SwingConstants;

import java.util.*;
import java.io.File;
import javax.swing.JFileChooser;
import javax.swing.filechooser.FileSystemView;


public class MainWindow extends JFrame
{
	private JTextField subject;
	private JTextField courseNumber;
	private JTextField sectionNumber;
	private JLabel subjectText;
	private JLabel courseText;
	private JLabel sectionText;
	private JLabel lblStatus;
	private JTextField link;
	
	private ArrayList<String> r_subject;
	private ArrayList<String> r_courseNumber;
	private ArrayList<String> r_sectionNumber;
	private ArrayList<String> r_link;
	
	// Main window Constructs the main GUI
	MainWindow()
	{
		r_subject = new ArrayList<String>();
		r_courseNumber = new ArrayList<String>();
		r_sectionNumber = new ArrayList<String>();

		JDialog mainBox = new JDialog(this,"Super Syllabus Generator");
		GridBagLayout gridLayout = new GridBagLayout();

		mainBox.getContentPane().setBackground(new Color(80,0,0));
		mainBox.getContentPane().setLayout(gridLayout);

		JPanel top = new JPanel();
		top.setLayout(new GridBagLayout());

		JPanel mid = new JPanel();
		mid.setLayout(new GridBagLayout());


		JPanel status = new JPanel();
		status.setLayout(new GridBagLayout());

		GridBagConstraints main = new GridBagConstraints();
		main.anchor = GridBagConstraints.NORTH;
		main.fill = GridBagConstraints.HORIZONTAL;
		main.weightx = .5;
		main.insets = new Insets(1,2,0,0);
		main.gridx = 0;
		main.gridy = 0;

		// TOP PANEL
		//=================================
		GridBagConstraints topPanel = new GridBagConstraints();
		subjectText = new JLabel("Enter your class subject.");
		topPanel.insets = new Insets(3,2,0,0);
		topPanel.gridx = 1;
		topPanel.gridy = 1;
		topPanel.gridwidth = 1;
		top.add(subjectText, topPanel);
		
		subject = new JTextField("CSCE");
		subject.setColumns(20);
		topPanel.gridx = 1;
		topPanel.gridy = 2;
		top.add(subject, topPanel);

		courseText = new JLabel("Enter your course number.");
		topPanel.gridx = 2;
		topPanel.gridy = 1;
		top.add(courseText,topPanel);
		
		courseNumber = new JTextField("121");
		courseNumber.setColumns(20);
		topPanel.gridx = 2;
		topPanel.gridy = 2;
		top.add(courseNumber, topPanel);
		
		sectionText = new JLabel("Enter your section number.");
		topPanel.gridx = 3;
		topPanel.gridy = 1;
		top.add(sectionText,topPanel);
		
		sectionNumber = new JTextField("507");
		sectionNumber.setColumns(20);
		topPanel.gridx = 3;
		topPanel.gridy = 2;
		top.add(sectionNumber,topPanel);
		



		// MID PANEL
		//============================

		GridBagConstraints midPanel = new GridBagConstraints();
		midPanel.anchor = GridBagConstraints.WEST;
		midPanel.insets = new Insets(2,1,0,0);
		midPanel.gridx = 1;
		midPanel.gridy = 1;
		midPanel.gridwidth = 1;
		JButton fileLoad = new JButton("Load in PDF");
		fileLoad.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JFileChooser jfc = new JFileChooser(FileSystemView.getFileSystemView().getDefaultDirectory());

				int returnValue = jfc.showOpenDialog(null);

				if (returnValue == JFileChooser.APPROVE_OPTION) {
					File selectedFile = jfc.getSelectedFile();
					link.setText(selectedFile.getAbsolutePath());
					System.out.println(selectedFile.getAbsolutePath());	
					
					r_subject.add(subjectText.getText());
					r_courseNumber.add(courseText.getText());
					r_sectionNumber.add(sectionText.getText());
					r_link.add(link.getText());
					
					}
				}
				});		
		mid.add(fileLoad,midPanel);
		midPanel.gridx = 2;
		link = new JTextField("None Selected");
		link.setColumns(60);
		mid.add(link,midPanel);
			

		// BOT PANEL
		//==============================
		GridBagConstraints botPanel = new GridBagConstraints();
		botPanel.anchor = GridBagConstraints.CENTER;
		botPanel.insets = new Insets(1,2,0,0);
		botPanel.gridx = 1;
		botPanel.gridy = 2;

		JButton Finish = new JButton("Generate Super Syllabus");
		Finish.addActionListener(new ActionListener() {
		public void actionPerformed(ActionEvent e) {
			JFileChooser jfc = new JFileChooser(FileSystemView.getFileSystemView().getHomeDirectory());

			int returnValue = jfc.showOpenDialog(null);

			if (returnValue == JFileChooser.APPROVE_OPTION) {
				File selectedFile = jfc.getSelectedFile();
				link.setText(selectedFile.getAbsolutePath());
				System.out.println(selectedFile.getAbsolutePath());	
				}
			}
			});		

		JButton generatePrimes = new JButton("Generate Primes");
		generatePrimes.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				lblStatus.setText("Generating Primes.");
			}
	    });
		

		//STATUS PANEL
		//================================================
		GridBagConstraints statusPanel = new GridBagConstraints();
		statusPanel.anchor = GridBagConstraints.WEST;
		statusPanel.weightx = .5;
		statusPanel.insets = new Insets(1,2,0,0);
		statusPanel.gridx = 0;
		statusPanel.gridy = 2;

		lblStatus = new JLabel("Keep Loading All Your Syllabi");
		status.add(lblStatus,statusPanel);

		mainBox.add(top,main);
		main.gridy = 1;
		mainBox.add(mid,main);
		main.gridy = 2;
		mainBox.add(status,main);


		mainBox.setSize(new Dimension(1000,400));
		mainBox.pack(); // Knowing what this is and why it is needed is important. You should read the documentation on this function!
		mainBox.setVisible(true);
		
	}


	// This function updates all the GUI statistics. (# of primes, # of crosses, etc)
//	private void updateStats()
//	{
//		
// 	}
	public ArrayList<String> getSubjects()
	{
		return r_subject;
	}
	public ArrayList<String> getCourseNumbers()
	{
		return r_courseNumber;
	}
	public ArrayList<String> getSectionNumbers()
	{
		return r_sectionNumber;
	}
	public ArrayList<String> getLinks()
	{
		return r_link;
	}

}
